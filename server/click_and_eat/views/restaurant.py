from ..forms import *
from .base_views import *
import json
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse


class CartProduct:
    def __init__(self, product_id, name, count):
        self.product_id = product_id
        self.name = name
        self.count = count

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    @classmethod
    def from_dict(cls, dictionary):
        return cls(**dictionary)

    def to_dict(self):
        return self.__dict__


class Cart:
    def __init__(self, products, **kwargs):
        self.products = []

        for product in products:
            self.products.append(CartProduct.from_dict(product))

    def find(self, product_id):
        products = list(filter(lambda x: x.product_id == product_id, self.products))

        if len(products) >= 1:
            return products[0]
        else:
            return None

    def append(self, product_id, name, count=1):
        product = self.find(product_id)
        if product is None:
            product = CartProduct(product_id, name, count)
            self.products.append(product)
        else:
            product.name = name
            product.count = product.count + count

        if product.count <= 0:
            self.products.remove(product)

    def remove(self, product_id):
        product = self.find(product_id)
        if product is not None:
            self.products.remove(product)

    def clear(self):
        self.products = []

    @classmethod
    def load(cls, request):
        cart = request.session.get('cart', Cart([]).to_dict())
        return Cart.from_dict(cart)

    def save(self, request):
        request.session['cart'] = self.to_dict()

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    @classmethod
    def from_dict(cls, dictionary):
        return cls(**dictionary)

    def to_dict(self):
        products = []
        products_ids = []

        for product in self.products:
            products_ids.append(product.product_id)
            products.append(product.to_dict())

        return {'products_ids': products_ids, 'products': products}


class RestaurantView(View):
    template_name = 'main/restaurant/restaurant.html'

    def get(self, request, restaurant_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        context = {'restaurant': restaurant}
        return render(request, self.template_name, context)


class CartViewComponent(View):
    template_name = 'templates/base/cart.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CartAdd(View):

    def get(self, request, product_id, count, *args, **kwargs):
        cart = Cart.load(request)

        product = get_object_or_404(Product, id=product_id)

        cart.append(product.id, product.name, count)
        cart.save(request)
        return HttpResponse('OK')


class CartDelete(View):

    def get(self, request, product_id, count,*args, **kwargs):
        cart = Cart.load(request)

        product = get_object_or_404(Product, id=product_id)

        cart.append(product.id, product.name, -count)
        cart.save(request)
        return HttpResponse('OK')


class CartRemove(View):

    def get(self, request, product_id, *args, **kwargs):
        cart = Cart.load(request)

        product = get_object_or_404(Product, id=product_id)

        cart.remove(product.id)
        cart.save(request)
        return HttpResponse('OK')

class CartClear(View):

    def get(self, request):
        cart = Cart.load(request)
        cart.clear()
        cart.save(request)
        return HttpResponse('OK')

