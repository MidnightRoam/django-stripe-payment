from django.urls import path

from .views import (
    NewsPageListView
)

urlpatterns = [
    path('', NewsPageListView.as_view(), name='news')
]
