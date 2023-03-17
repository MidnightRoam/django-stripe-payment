from django.urls import path

from .views import (
    CartPageView,
)

urlpatterns = [
    path('', CartPageView.as_view(), name='cart'),
]
