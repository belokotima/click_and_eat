from ..forms import *
from .base_views import *
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404


class Restaurateur(LoginRequiredView):
    template_name = 'restaurateur/restaurateur_welcome.html'

    def get(self, request, *args, **kwargs):
        restaurants = Restaurant.objects.filter(owner=request.user)

        if len(restaurants) == 0:
            return render(request, self.template_name)
        else:
            return redirect('restaurateur_dashboard')


class RestaurateurDashboard(LoginRequiredView):
    template_name = 'restaurateur/dashboard.html'

    def get(self, request, *args, **kwargs):
        restaurants = Restaurant.objects.filter(owner=request.user)

        if len(restaurants) > 0:
            context = {'restaurants': restaurants}
            return render(request, self.template_name, context)
        else:
            return redirect('restaurateur')


class RestaurantDashboard(LoginRequiredView):
    template_name = 'restaurateur/restaurant/dashboard.html'

    def get(self, request, restaurant_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id, owner=request.user)
        context = {'restaurant': restaurant}
        return render(request, self.template_name, context)


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
            return redirect('restaurateur_dashboard')
        return render(request, self.template_name)


class RestaurantEdit(LoginRequiredView):
    template_name = 'restaurateur/register.html'

    def get(self, request, restaurant_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        form = RestaurantEditForm(instance=restaurant)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, restaurant_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        form = RestaurantEditForm(request.POST, request.FILES, instance=restaurant)
        form.instance.owner = request.user
        if form.is_valid():
            form.save()
            return redirect('restaurant_dashboard', restaurant_id=restaurant_id)
        return render(request, self.template_name)


class RestaurantMenuAdd(LoginRequiredView):
    template_name = 'restaurateur/restaurant/add_product.html'

    def get(self, request, restaurant_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id, owner=request.user)
        form = RestaurantMenuAddForm()
        context = {'form': form, 'restaurant': restaurant}
        return render(request, self.template_name, context)

    def post(self, request, restaurant_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id, owner=request.user)
        form = RestaurantMenuAddForm(request.POST, request.FILES)
        form.instance.restaurant_id = restaurant.id
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, self.template_name)
