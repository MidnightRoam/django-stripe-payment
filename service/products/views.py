import stripe
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import Q, Count, Sum
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView

from .models import Item, Order, Tag, Customer

stripe.api_key = settings.STRIPE_SECRET_KEY


class IndexPageView(ListView):
    """Index page view"""
    model = Item
    template_name = 'products/index.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Paginator(Tag.objects.all().annotate(product_count=Count('item')), self.paginate_by)
        search_query = self.request.GET.get('q')
        if search_query:
            items = Item.objects\
                .filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))\
                .prefetch_related('tags')
        else:
            items = Item.objects.all().prefetch_related('tags')
        context.update({
            'items': items,
            'tags': p.page(context['page_obj'].number),
            'title': 'Our products'
        })
        return context


class TagSortPageView(ListView):
    """Product sort by tags page view"""
    model = Item
    template_name = 'products/sorted_items.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Paginator(Tag.objects.all().annotate(product_count=Count('item')), self.paginate_by)
        context.update({
            'items': Item.objects.filter(tags__pk=self.kwargs['pk']).prefetch_related('tags'),
            'tags': p.page(context['page_obj'].number),
            'title': 'Sorted products'
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


class ProductPageDetailView(DetailView):
    """Product page view"""
    template_name = 'products/item_page.html'
    model = Item

    def post(self, request, pk):
        item = Item.objects.get(pk=pk)
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer)
        order.item.add(item.id)
        order.save()

        return redirect('cart')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
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


class CartPageView(ListView):
    """Cart page view"""
    template_name = 'products/cart_page.html'

    def get(self, request, *args, **kwargs):
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        cart, _ = Order.objects.get_or_create(customer=customer)
        items = cart.item.all()
        total_amount = cart.item.aggregate(total_amount=Sum('price') / 100)['total_amount']

        return render(request, 'products/cart_page.html', {
            'cart': cart,
            'items': items,
            'total_amount': total_amount,
            'title': 'Your cart'
        })

    def post(self, request, *args, **kwargs):
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Item, id=item_id)
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        cart, _ = Order.objects.get_or_create(customer=customer)
        cart_item = Item.objects.get(order=cart, id=item.id)
        cart.item.remove(cart_item)
        cart.save()

        return redirect('cart')


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
