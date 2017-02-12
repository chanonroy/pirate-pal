from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

# class RegistrationForm(UserCreationForm):
#
#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")
