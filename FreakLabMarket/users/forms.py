from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True,
                                      'placeholder': 'Username or Email',}))
    password = forms.CharField(
        widget=forms.TextInput(attrs={"autocomplete": "current-password",
                                      'placeholder': 'Password',}))

    class Meta:
        model = User