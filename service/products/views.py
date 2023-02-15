import stripe
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView

from .models import Item, Order

stripe.api_key = settings.STRIPE_SECRET_KEY


class IndexPageView(ListView):
    """Index page view"""
    model = Item
    template_name = 'products/index.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Paginator(Item.objects.all(), self.paginate_by)
        context.update({
            'items': p.page(context['page_obj'].number),
            'title': 'Our products'
        })
        return context


class SuccessView(TemplateView):
    """Success order page view"""
    template_name = 'products/success_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Success order'
        })
        return context


class CancelView(TemplateView):
    """Cancel order page view"""
    template_name = 'products/cancel_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Cancel order'
        })
        return context


class ProductPageView(TemplateView):
    """Product page view"""
    template_name = 'products/item_page.html'

    def get_context_data(self, **kwargs):
        item = Item.objects.get(pk=self.kwargs["pk"])
        context = super(ProductPageView, self).get_context_data(**kwargs)
        context.update({
            'item': item,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
            'title': 'Product details'
        })
        return context


class CreateCheckoutSessionView(View):
    """Create checkout session view"""
    def get(self, *args, **kwargs):
        item = Item.objects.get(pk=self.kwargs["pk"])
        YOUR_DOMAIN = 'http://127.0.0.1:8000/'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                            'description': item.description
                        }
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + 'success/',
            cancel_url=YOUR_DOMAIN + 'cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })

    def post(self, request, *args, **kwargs):
        item = Item.objects.get(pk=self.kwargs["pk"])
        YOUR_DOMAIN = 'http://127.0.0.1:8000/'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                            'description': item.description
                        }
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                'item_id': item.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + 'success/',
            cancel_url=YOUR_DOMAIN + 'cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


class CartPageView(View):
    """Cart page view"""
    template_name = 'products/cart_page.html'

    def get(self, request, *args, **kwargs):
        cart = Order.objects.all()

        return render(request, 'products/cart_page.html', {
            'cart': cart,
            'title': 'Your cart'
        })

    def post(self, request, *args, **kwargs):
        pass


@csrf_exempt
def stripe_webhook(request):
    """Stripe webhook view"""
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.

        session = stripe.checkout.Session.retrieve(
            event['data']['object']['id'],
            expand=['line_items'],
        )

        customer_email = session['customer_details']['email']
        item_id = session['metadata']['item_id']

        item = Item.objects.get(id=item_id)

        send_mail(
            subject='Thank you for your purchase!',
            message=f'Your order for "{item.name}" has been completed.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[customer_email]
        )

        print(session)
    # Passed signature verification
    return HttpResponse(status=200)
