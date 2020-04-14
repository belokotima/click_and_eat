from django import forms
from django.forms import ModelForm
from .models import Restaurant


class LoginForm(forms.Form):
    username = forms.CharField(max_length=12)
    password = forms.CharField(widget=forms.PasswordInput())
    remember_me = forms.BooleanField(required=False)


class RegisterForm(LoginForm):
    first_name = forms.CharField(max_length=12)
    email = forms.EmailField()
    repeat_password = forms.CharField(widget=forms.PasswordInput())


class RestaurantMenuForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'
