import os
from django import forms
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

auth_templates_dir = 'auth'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=12)
    password = forms.CharField(widget=forms.PasswordInput())
    remember_me = forms.BooleanField(required=False)


class RegisterForm(LoginForm):
    first_name = forms.CharField(max_length=12)
    email = forms.EmailField()
    repeat_password = forms.CharField(widget=forms.PasswordInput())


class Login(View):
    template_name = os.path.join(auth_templates_dir, 'login.html')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        context = {}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']

            if self.login(request, username, password, remember_me):
                return redirect('index')
            else:
                context['error'] = 'Неверный логин или пароль'
                return render(request, self.template_name, context)
        else:
            context['error'] = 'Неверный формат ввода'
            return render(request, self.template_name, context)

    @staticmethod
    def login(request, username, password, remember_me):
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)
            return True
        else:
            return False


class Register(View):
    template_name = os.path.join(auth_templates_dir, 'register.html')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        context = {}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            repeat_password = form.cleaned_data['repeat_password']
            first_name = form.cleaned_data['first_name']
            remember_me = form.cleaned_data['remember_me']

            try:
                User.objects.get(username=username)
                context['error'] = 'Username занят'
            except:
                try:
                    User.objects.get(email=email)
                    context['error'] = 'E-mail занят'
                except:
                    if password != repeat_password:
                        context['error'] = 'Пароли не совпадают'
                    else:
                        try:
                            User.objects.create_user(username=username, email=email, password=password,
                                                     first_name=first_name)
                            if Login.login(request, username, password, remember_me):
                                return redirect('index')
                            else:
                                context['error'] = 'Неверный логин или пароль'
                        except:
                            context['error'] = 'Ошибка при регистрации'
                
            return render(request, self.template_name, context)
            
        else:
            context['error'] = 'Неверный формат ввода'
            return render(request, self.template_name, context)
