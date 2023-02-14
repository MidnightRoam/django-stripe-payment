from django.urls import path

from .views import (
    CreateCheckoutSessionView,
    ProductPageView,
    SuccessView,
    CancelView,
    IndexPageView,
    CartPageView,
    stripe_webhook
)

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('item/<int:pk>/', ProductPageView.as_view(), name='item_detail'),
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('cart/', CartPageView.as_view(), name='cart'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
]