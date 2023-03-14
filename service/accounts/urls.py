from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import (
    SignInLoginView,
    SignUpCreateView,
    LogoutView
)

urlpatterns = [
    path('login/', SignInLoginView.as_view(), name='login'),
    path('signup/', SignUpCreateView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]