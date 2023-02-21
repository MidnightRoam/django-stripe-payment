from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, forms
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


# class UserLoginForm(ModelForm):
#
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#         labels = {
#             'username': "Username",
#             'password': 'Password'
#         }
#         widgets = {
#             "username": forms.TextInput(
#                 attrs={'class': 'login__input', 'type': 'text'}
#             ),
#             "password": forms.PasswordInput(
#                 attrs={'class': 'login__input', 'type': 'password'}
#             )
#         }
#
#     def __init__(self, request=None, *args, **kwargs):
#         self.request = request
#         super().__init__(*args, **kwargs)
#
#     def get_user(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#         return authenticate(request=self.request, username=username, password=password)


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
