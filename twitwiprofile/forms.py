from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    username = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password1 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(
        attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))

    class Meta:
        fields = ['email', 'username', 'first_name',
                  'last_name', 'password1', 'password2']
        model = User


class SignInForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(required=True, widget=forms.widgets.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control'}))
