from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Your Name"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'placeholder': "Your Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': "Repeat Your Password"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
