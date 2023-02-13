from django.contrib import admin
from django.urls import path

from products.views import (
    CreateCheckoutSessionView,
    ProductPageView,
    SuccessView,
    CancelView,
    IndexPageView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view(), name='index'),
    path('item/<int:pk>/', ProductPageView.as_view(), name='item_page'),
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel')
]
