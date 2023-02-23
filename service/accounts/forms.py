from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'login__input'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'login__input'
            }
        )
    )


class UserSignupForm(ModelForm):
    username = forms.CharField(
        help_text='',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'login__input'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        labels = {
            'username': 'Username',
            'first_name': "First name",
            'last_name': "Last name",
            'email': "Email",
            'password': 'Password'
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={'class': 'login__input', 'type': 'text'}
            ),
            "last_name": forms.TextInput(
                attrs={'class': 'login__input', 'type': 'text'}
            ),
            "email": forms.EmailInput(
                attrs={'class': 'login__input', 'type': 'email'}
            ),
            "password": forms.PasswordInput(
                attrs={'class': 'login__input', 'type': 'password'}
            )
        }
