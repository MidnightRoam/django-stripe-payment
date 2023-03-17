from django.urls import path

from .views import (
    NewsPageListView
)

urlpatterns = [
    path('all/', NewsPageListView.as_view(), name='news'),
    path('<slug:slug>/', NewsPageListView.as_view(), name='tags-news')
]
