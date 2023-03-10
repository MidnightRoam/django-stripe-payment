from django.urls import path

from .views import (
    CreateCheckoutSessionView,
    ProductPageDetailView,
    SuccessView,
    CancelView,
    IndexPageView,
    CartPageView,
    TagSortPageListView,
    PlatformSortPageListView,
    AddToFavoritesView,
    DeleteFromFavoritesView,
    ItemRatingDetailView,
    AddReviewView,
    stripe_webhook,
)

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('item/<int:pk>/', ProductPageDetailView.as_view(), name='item_detail'),
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('items/<int:pk>/', TagSortPageListView.as_view(), name='items_sort'),
    path('platform/<slug:slug>/', PlatformSortPageListView.as_view(), name='platform_sort'),
    path('add-to-favorites/<int:pk>/', AddToFavoritesView.as_view(), name='add_to_favorites'),
    path('delete-from-favorites/<int:pk>/', DeleteFromFavoritesView.as_view(), name='delete_from_favorites'),
    path('item/<int:item_id>/reviews', ItemRatingDetailView.as_view(), name='reviews'),
    path('item/<int:pk>/reviews/add', AddReviewView.as_view(), name='add_review'),
    path('search/', IndexPageView.as_view(), name='search'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('cart/', CartPageView.as_view(), name='cart'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
]
