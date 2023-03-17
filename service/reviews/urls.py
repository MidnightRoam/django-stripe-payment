from django.urls import path

from .views import (
    ItemRatingDetailView,
    AddReviewView
)

urlpatterns = [
    path('<slug:slug>/all', ItemRatingDetailView.as_view(), name='reviews'),
    path('<int:pk>/reviews/add', AddReviewView.as_view(), name='add_review'),
]
