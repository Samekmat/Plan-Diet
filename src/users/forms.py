from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ["username", "email", "password1", "password2", "age", "height", "weight", "sex"]


class LoginForm(forms.Form):
    login = forms.CharField(label="Your login", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Your password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
