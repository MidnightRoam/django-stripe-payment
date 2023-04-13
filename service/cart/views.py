from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
import stripe

from .models import Order
from products.models import Customer, Favorite, Item


class CartPageView(LoginRequiredMixin, ListView):
    """Cart page view"""
    template_name = 'cart/cart_page.html'
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        cart, _ = Order.objects.get_or_create(customer=customer)
        items = cart.item.all().prefetch_related('languages')
        total_amount = cart.item.aggregate(total_amount=Sum('price') / 100)['total_amount']
        favorites = Favorite.objects.filter(user=request.user).select_related('item')

        return render(request, 'cart/cart_page.html', {
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


class CreateCheckoutSessionView(View):
    """Create cart checkout session view"""
    domain = 'http://127.0.0.1:8000/'

    def post(self, request, *args, **kwargs):
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)
        line_items = []
        cart = Order.objects.get_or_create(customer=customer)
        DOMAIN = self.domain
        for item_id, amount in cart.items():
            item = Item.objects.get(pk=item_id)
            price = Item.get_price_stripe()
            line_items.append({
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': price,
                        'product_data': {
                            'name': item.name,
                            'description': item.description
                        }
                    },
                    'quantity': 1,
                },
            })

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=DOMAIN + 'success/',
            cancel_url=DOMAIN + 'cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })