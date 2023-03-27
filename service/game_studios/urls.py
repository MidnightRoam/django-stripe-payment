from django.urls import path

from .views import (
    PublisherDetailView,
    DeveloperDetailView
)

urlpatterns = [
    path('publisher/<slug:slug>/', PublisherDetailView.as_view(), name='publisher'),
    path('developer/<slug:slug>/', DeveloperDetailView.as_view(), name='developer'),
]
