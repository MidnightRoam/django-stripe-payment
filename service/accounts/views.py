from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView

from accounts.forms import UserLoginForm, UserSignupForm


class SignInLoginView(LoginView):
    """User login view"""
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sign In'
        return context

    def get_success_url(self):
        return reverse_lazy('index')


class SignUpCreateView(CreateView):
    """User sign up view"""
    template_name = 'accounts/registration.html'
    form_class = UserSignupForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sign Up'
        return context

    def form_valid(self, form):
        """Login the user after successful registration"""
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LogoutView(View):
    """User logout view"""
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')
