import stripe
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import Q, Count, Sum, OuterRef, Exists, Avg
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView

from .forms import ItemRatingForm
from .models import Item, Order, Tag, Customer, Favorite, ItemScreenshot, ItemRating

stripe.api_key = settings.STRIPE_SECRET_KEY


class IndexPageView(ListView):
    """Index page view"""
    model = Item
    template_name = 'products/index.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Выводим только те теги, за которыми закреплен хотя бы 1 продукт
        p = Paginator(Tag.objects.exclude(item__isnull=True).annotate(product_count=Count('item')), self.paginate_by)
        search_query = self.request.GET.get('q')
        if search_query:
            items = Item.objects \
                .filter(Q(name__icontains=search_query) | Q(description__icontains=search_query)) \
                .prefetch_related('tags')
        else:
            items = Item.objects.prefetch_related('tags', 'discounts').all()
        context.update({
            'items': items,
            'tags': p.page(context['page_obj'].number),
            'title': 'Games',
        })
        return context


class TagSortPageView(ListView):
    """Product sort by tags page view"""
    model = Item
    template_name = 'products/sorted_items.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Paginator(Tag.objects.exclude(item__isnull=True).annotate(product_count=Count('item')), self.paginate_by)
        tag = Tag.objects.get(pk=self.kwargs['pk'])
        context.update({
            'items': Item.objects.filter(tags__pk=self.kwargs['pk']).prefetch_related('tags'),
            'tags': p.page(context['page_obj'].number),
            'title': f'{tag} games'
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
    template_name = 'products/item_detail_page.html'
    model = Item
    context_object_name = 'item'

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
        added_to_favorites = Favorite.objects.filter(item=self.object).count()
        product_rating = ItemRating.objects.filter(item=self.object).aggregate(Avg('rate'))
        title = Item.objects.get(pk=self.kwargs['pk']).name
        context.update({
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
            'title': f'{title}',
            'added_to_favorites': added_to_favorites,
            'product_rating': product_rating
        })
        return context


class CreateCheckoutSessionView(View):
    """Create checkout session view"""
    domain = 'http://127.0.0.1:8000/'

    def post(self, request, *args, **kwargs):
        item = Item.objects.get(pk=self.kwargs["pk"])
        DOMAIN = self.domain
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.get_price_stripe(),
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
            success_url=DOMAIN + 'success/',
            cancel_url=DOMAIN + 'cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


class CartPageView(LoginRequiredMixin, ListView):
    """Cart page view"""
    template_name = 'products/cart_page.html'
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        cart, _ = Order.objects.get_or_create(customer=customer)
        items = cart.item.all()
        total_amount = cart.item.aggregate(total_amount=Sum('price') / 100)['total_amount']
        favorites = Favorite.objects.filter(user=request.user).select_related('item')

        return render(request, 'products/cart_page.html', {
            'cart': cart,
            'items': items,
            'total_amount': total_amount,
            'favorites': favorites,
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


class AddToFavoritesView(LoginRequiredMixin, View):
    """Add product to favorites view"""
    login_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Item, id=item_id)
        favorite = Favorite.objects.get_or_create(user=request.user, item=item)
        return redirect('item_detail', pk=item.id)


class DeleteFromFavoritesView(View):
    """Delete product from favorites view"""

    def post(self, request, *args, **kwargs):
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Item, id=item_id)
        favorite = Favorite.objects.delete(user=request.user, item=item)
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


class ItemRatingDetailView(DetailView):
    """Item rating detail view"""
    template_name = 'products/reviews_form.html'
    login_url = reverse_lazy('login')

    def get(self, *args, **kwargs):
        current_item = Item.objects.get(id=self.kwargs['item_id'])
        context = {
            'item': current_item,
            'title': f'{current_item} Reviews',
        }
        return render(self.request, self.template_name, context)


class AddReviewView(LoginRequiredMixin, View):
    """Add review view"""
    def post(self, request, pk, *args, **kwargs):
        form = ItemRatingForm(request.POST)
        item = get_object_or_404(Item, pk=pk)
        if form.is_valid():
            # Проверяем, делал ли пользователь ранее отзыв на этот продукт
            if ItemRating\
                    .objects\
                    .filter(user=self.request.user)\
                    .filter(item_id=item)\
                    .exists():
                return redirect('reviews', item_id=item.id)  # Если да, то редирект
                # на страницу с обзорами этого продукта
            # Save form data to the database
            rating = form.save(commit=False)
            rating.item = item
            rating.user = request.user
            rating.rate = form.cleaned_data['rate']
            rating.text = form.cleaned_data['text']
            rating.save()
            return redirect('reviews', item_id=item.id)
        else:
            return redirect('index')
