from django.urls import path

from .views import (
    CartPageView,
    CreateCheckoutSessionView,
)

urlpatterns = [
    path('', CartPageView.as_view(), name='cart'),
    path('create-checkout/', CreateCheckoutSessionView.as_view(), name='create-checkout'),
]
