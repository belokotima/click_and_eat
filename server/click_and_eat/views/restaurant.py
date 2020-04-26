from ..forms import *
from .base_views import *
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404


class RestaurantView(View):
    template_name = 'main/restaurant/restaurant.html'

    def get(self, request, restaurant_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        context = {'restaurant': restaurant}
        return render(request, self.template_name, context)


class RestaurantAddToCart(View):

    def get(self, request, restaurant_id, product_id, *args, **kwargs):
        cart = request.session.get('cart', [])
        product = get_object_or_404(Product, restaurant_id=restaurant_id, id=product_id)
        product_context = {'name': product.name}

        cart.append(product_context)
        request.session['cart'] = cart
        return redirect('restaurant', restaurant_id=restaurant_id)
