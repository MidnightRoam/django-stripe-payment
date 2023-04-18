from django.urls import path

from .views import (
    CreateCheckoutSessionView,
    ProductPageDetailView,
    SuccessView,
    CancelView,
    IndexPageView,
    AddToFavoritesView,
    DeleteFromFavoritesView,
    GameSeriesListView,
    GameSeriesDetailView,
    JsonFilterGamesView,
    FilterGamesListView
)

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('games/<slug:tag_slug>/', IndexPageView.as_view(), name='index'),
    path('games/<slug:genre_slug>/', IndexPageView.as_view(), name='index'),
    path('platforms/<slug:platform_slug>/', IndexPageView.as_view(), name='index'),
    path('series/', GameSeriesListView.as_view(), name='series_list'),
    path('series/<slug:series_slug>/', GameSeriesDetailView.as_view(), name='series_detail'),
    path('game/<int:pk>/', ProductPageDetailView.as_view(), name='item_detail'),
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('add-to-favorites/<int:pk>/', AddToFavoritesView.as_view(), name='add_to_favorites'),
    path('delete-from-favorites/<int:pk>/', DeleteFromFavoritesView.as_view(), name='delete_from_favorites'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('json-filter/', JsonFilterGamesView.as_view(), name='json_filter'),
    path('filter/', FilterGamesListView.as_view(), name='filter'),
]
