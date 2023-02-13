import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class IndexPageView(ListView):
    """Index page view"""
    model = Item
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context


class SuccessView(TemplateView):
    """Success order page view"""
    template_name = 'products/success_page.html'


class CancelView(TemplateView):
    """Cancel order page view"""
    template_name = 'products/cancel_page.html'


class ProductPageView(TemplateView):
    """Product page view"""
    template_name = 'products/item_page.html'

    def get_context_data(self, **kwargs):
        item = Item.objects.get(pk=self.kwargs["pk"])
        context = super(ProductPageView, self).get_context_data(**kwargs)
        context.update({
            'item': item,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
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
            mode='payment',
            success_url=YOUR_DOMAIN + 'success/',
            cancel_url=YOUR_DOMAIN + 'cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })
