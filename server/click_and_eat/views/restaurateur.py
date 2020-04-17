import os
from ..forms import *
from .base_views import *
from django.views import View
from django.shortcuts import render, redirect


class Restaurateur(LoginRequiredView):
    template_name = 'restaurateur/restaurateur_welcome.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RestaurantRegister(LoginRequiredView):
    template_name = 'restaurateur/register_form.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RestaurantCreate(LoginRequiredView):
    template_name = 'restaurateur/register.html'

    def get(self, request, *args, **kwargs):
        form = RestaurantEditForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RestaurantEditForm(request.POST, request.FILES)
        form.instance.owner = request.user
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, self.template_name)


class RestaurantMenu(View):

    template_name = 'restaurateur/restaurant.html'

    def get(self, request, restaurante_id, *args, **kwargs):
        restaurant = Restaurant.objects.get(id=restaurante_id)
        products = restaurant.product_set.all()
        context = {'products': products}
        return render(request, self.template_name, context)


class RestaurantMenuAdd(LoginRequiredView):
    template_name = 'restaurateur/menu.html'

    def get(self, request, *args, **kwargs):
        form = RestaurantMenuAddForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RestaurantMenuAddForm(request.POST, request.FILES)
        form.instance.restaurant_id = request.user.id
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, self.template_name)
