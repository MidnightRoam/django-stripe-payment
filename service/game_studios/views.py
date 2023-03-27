from django.shortcuts import render
from django.views.generic import DetailView

from .models import Publisher, Developer


class PublisherDetailView(DetailView):
    """Game publisher detail page view"""
    model = Publisher
    template_name = 'game_studios/publisher_detail.html'
    context_object_name = 'publisher'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     added_to_favorites = Favorite.objects.filter(item=self.object).count()
    #     product_rating = ItemRating.objects.filter(item=self.object).aggregate(Avg('rate'))
    #     title = Item.objects.get(pk=self.kwargs['pk']).name
    #     dlc = ItemDLC.objects.filter(product=self.object)
    #     context.update({
    #         'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
    #         'title': f'{title}',
    #         'added_to_favorites': added_to_favorites,
    #         'product_rating': product_rating,
    #         'dlc': dlc
    #     })
    #     return context


class DeveloperDetailView(DetailView):
    """Game developer detail page view"""
    model = Developer
    template_name = 'game_studios/developer_detail.html'
    context_object_name = 'developer'
