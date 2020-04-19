from ..forms import *
from .base_views import *
from django.views import View
from django.shortcuts import render, redirect


class RestaurantView(View):
    template_name = 'main/restaurant/restaurant.html'

    def get(self, request, restaurant_id, *args, **kwargs):
        restaurant = Restaurant.objects.get(id=restaurant_id)
        products = restaurant.product_set.all()
        context = {'products': products, 'restaurant': restaurant}
        return render(request, self.template_name, context)