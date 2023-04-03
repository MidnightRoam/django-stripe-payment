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

from .models import Item, Tag, Customer, Favorite, ItemScreenshot, ItemPlatform, ItemDLC, Genre
from game_studios.models import Developer, Publisher
from cart.models import Order
from reviews.models import ItemRating

stripe.api_key = settings.STRIPE_SECRET_KEY


class IndexPageView(ListView):
    """
    Output of all products, or output of filtered
    products by criteria: platform, tag
    """
    model = Item
    template_name = 'products/index.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Выводим только те теги, за которыми закреплен хотя бы 1 продукт
        p = Paginator(Tag.objects.exclude(item__isnull=True).annotate(product_count=Count('item')), self.paginate_by)
        platforms = ItemPlatform.objects.all()
        search_query = self.request.GET.get('q')
        tag = self.kwargs.get('tag_slug')
        platform = self.kwargs.get('platform_slug')
        items = Item.objects.prefetch_related('tags', 'discounts', 'platform').all()
        developers = Developer.objects.all()
        total_developers = Developer.objects.all().count()
        publishers = Publisher.objects.all()
        total_publishers = Publisher.objects.all().count()
        genres = Genre.objects.all()
        total_games = Item.objects.all().count()
        title = 'Pixel Playground'

        if tag:  # returns a list of products filtered by chosen tag
            items = Item.objects.prefetch_related('tags', 'discounts', 'platform').filter(tags__slug=tag)
            title_tag = tag.capitalize()
            title = f'{title_tag} games'

        if platform:  # returns a list of products filtered by chosen platform
            items = Item.objects.prefetch_related('tags', 'discounts', 'platform').filter(platform__slug=platform)
            title_platform = platform.capitalize()
            title = f'{title_platform} games'

        if search_query:  # returns a list of products filtered by search query
            items = Item.objects \
                .filter(Q(name__icontains=search_query) | Q(description__icontains=search_query)) \
                .prefetch_related('tags', 'discounts', 'platform')
            title = 'Search results'

        context.update({
            'items': items,
            'developers': developers,
            'publishers': publishers,
            'total_developers': total_developers,
            'total_publishers': total_publishers,
            'genres': genres,
            'total_genres': total_games,
            'tags': p.page(context['page_obj'].number),
            'platforms': platforms,
            'title': title,
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
        dlc = ItemDLC.objects.filter(product=self.object)
        context.update({
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
            'title': f'{title}',
            'added_to_favorites': added_to_favorites,
            'product_rating': product_rating,
            'dlc': dlc
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
