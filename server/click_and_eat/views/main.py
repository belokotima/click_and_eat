from ..forms import *
from .base_views import *
import json
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .cart import *


class Checkout(LoginRequiredView):
    template_name = 'main/checkout.html'

    def get(self, request, *args, **kwargs):
        form = CheckoutForm()
        cart = Cart.load(request)
        restaurant = get_object_or_404(Restaurant, id=cart.restaurant_id)
        form.set_restaurant(restaurant)
        context = {'restaurant': restaurant, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CheckoutForm(request.POST)
        cart = Cart.load(request)
        restaurant = get_object_or_404(Restaurant, id=cart.restaurant_id)
        form.set_restaurant(restaurant)

        if form.is_valid():
            address = get_object_or_404(AddressOfRestaurant, id=form.cleaned_data['address'].id)
            order = Order(customer=request.user,
                          restaurant=address,
                          total=cart.total,
                          pickup_time=form.cleaned_data['pickup_time'],
                          instant=form.cleaned_data['instant'],
                          finished=False,
                          canceled=False,
                          in_progress=False,
                          ready=False)

            order.save()

            for cart_product in cart.products:
                product = get_object_or_404(Product, id=cart_product.product_id)
                order.add_product(product, cart_product.count, cart_product.price, cart_product.total)

            address.set_order_codes(order)

            cart.clear()
            cart.save(request)
            return redirect('order', order_id=order.id)
        else:
            context = {'form': form}
            return render(request, self.template_name, context)


class OrderView(LoginRequiredView):
    template_name = 'main/order.html'

    def get(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, id=order_id, customer=request.user)
        context = {'restaurant': order.restaurant.restaurant, 'order': order}
        return render(request, self.template_name, context)


class OrderContentsView(LoginRequiredView):
    template_name = 'main/base/order_base.html'

    def get(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, id=order_id, customer=request.user)
        context = {'restaurant': order.restaurant.restaurant, 'order': order}
        return render(request, self.template_name, context)
