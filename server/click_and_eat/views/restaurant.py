from ..forms import *
from .base_views import *
import json
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse


class CartProduct:
    def __init__(self, product_id, name, price, count, **kwargs):
        self.product_id = product_id
        self.name = name
        self.count = count
        self.price = price
        self.total = self.price * self.count

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
    def __init__(self, products, total, **kwargs):
        self.products = []
        self.total = total
        for product in products:
            self.products.append(CartProduct.from_dict(product))

    def find(self, product_id):
        products = list(filter(lambda x: x.product_id == product_id, self.products))

        if len(products) >= 1:
            return products[0]
        else:
            return None

    def append(self, product, count=1):
        cart_product = self.find(product.id)
        if cart_product is None:
            cart_product = CartProduct(product.id, product.name, product.price, count)
            self.products.append(cart_product)
        else:
            cart_product.name = product.name
            cart_product.count = cart_product.count + count

        if cart_product.count <= 0:
            self.products.remove(cart_product)

    def remove(self, product_id):
        product = self.find(product_id)
        if product is not None:
            self.products.remove(product)

    def clear(self):
        self.products = []

    @classmethod
    def load(cls, request):
        cart = request.session.get('cart', Cart([], 0).to_dict())
        return Cart.from_dict(cart)

    def save(self, request):
        self.total = sum([product.count * product.price for product in self.products])
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

        return {'products_ids': products_ids, 'products': products, 'total': self.total}


class RestaurantView(View):
    template_name = 'main/restaurant/restaurant.html'

    def get(self, request, restaurant_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        context = {'restaurant': restaurant}
        return render(request, self.template_name, context)


class CartViewComponent(View):
    template_name = 'base/cart_contents.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CartAdd(View):

    def get(self, request, product_id, count, *args, **kwargs):
        cart = Cart.load(request)

        product = get_object_or_404(Product, id=product_id)

        cart.append(product, count)
        cart.save(request)
        return redirect('cart_view')


class CartDelete(View):

    def get(self, request, product_id, count,*args, **kwargs):
        cart = Cart.load(request)

        product = get_object_or_404(Product, id=product_id)

        cart.append(product, -count)
        cart.save(request)
        return redirect('cart_view')


class CartRemove(View):

    def get(self, request, product_id, *args, **kwargs):
        cart = Cart.load(request)

        product = get_object_or_404(Product, id=product_id)

        cart.remove(product.id)
        cart.save(request)
        return redirect('cart_view')


class CartClear(View):

    def get(self, request):
        cart = Cart.load(request)
        cart.clear()
        cart.save(request)
        return redirect('cart_view')

