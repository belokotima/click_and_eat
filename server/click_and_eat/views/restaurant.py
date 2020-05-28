from ..forms import *
from .base_views import *
import json
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .cart import *


class RestaurantView(View):
    template_name = 'main/restaurant/restaurant.html'

    def get(self, request, restaurant_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        context = {'restaurant': restaurant}
        return render(request, self.template_name, context)


class RestaurantAddressView(View):

    def get(self, request, *args, **kwargs):
        address_id = request.GET.get('address', None)
        if address_id is not None:
            address = get_object_or_404(AddressOfRestaurant, id=address_id)
            cart = Cart.load(request)
            cart.set_address(address)
            cart.save(request)
            return redirect('restaurant', restaurant_id=address.restaurant.id)
        else:
            return redirect('index')
