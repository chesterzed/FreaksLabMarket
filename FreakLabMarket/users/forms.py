from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True,
                                      'placeholder': 'Username or Email',}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                      'placeholder': 'Password',}))

    class Meta:
        model = User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'bio',
        ]
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    bio = forms.Textarea()


class ProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)

    class Meta:
        model = User
        fields = [
            'image',
            # 'background_image',
            'first_name',
            'last_name',
            'username',
            'email',
            'bio',
            'newsletter',
            'notifications',
        ]
    # image = forms.ImageField(required=False)
    # background_image = forms.ImageField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea(attrs={'required': False,}))
    newsletter = forms.CheckboxInput()
    notifications = forms.CheckboxInput()
