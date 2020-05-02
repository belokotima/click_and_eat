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
        context = {'form': form, 'restaurant': restaurant, 'edit': True}
        return render(request, self.template_name, context)

    def post(self, request, restaurant_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        form = RestaurantEditForm(request.POST, request.FILES, instance=restaurant)
        form.instance.owner = request.user
        if form.is_valid():
            form.save()
            return redirect('restaurant_dashboard', restaurant_id=restaurant_id)
        context = {'form': form, 'restaurant': restaurant, 'edit': True}
        return render(request, self.template_name, context)


class RestaurantAddProduct(LoginRequiredView):
    template_name = 'restaurateur/restaurant/product.html'

    def get(self, request, restaurant_id, product_id=None, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id, owner=request.user)

        product = None

        if product_id is not None:
            product = get_object_or_404(Product, pk=product_id, restaurant=restaurant)
            form = RestaurantAddProductForm(instance=product)
        else:
            form = RestaurantAddProductForm()

        form.set_restaurant(restaurant)

        context = {'form': form, 'restaurant': restaurant, 'edit': product_id, 'product': product}
        return render(request, self.template_name, context)

    def post(self, request, restaurant_id, product_id=None, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id, owner=request.user)

        if product_id is not None:
            product = get_object_or_404(Product, pk=product_id, restaurant=restaurant)
            form = RestaurantAddProductForm(request.POST, request.FILES, instance=product)
        else:
            form = RestaurantAddProductForm(request.POST, request.FILES)

        form.set_restaurant(restaurant)

        form.instance.restaurant_id = restaurant.id
        if form.is_valid():
            form.save()
            return redirect('restaurant_dashboard', restaurant_id=restaurant_id)
        return render(request, self.template_name)


class RestaurantDeleteProduct(LoginRequiredView):
    template_name = ''

    def get(self, request, restaurant_id, product_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id, owner=request.user)
        product = get_object_or_404(Product, pk=product_id, restaurant=restaurant)

        product.delete()

        return redirect('restaurant_dashboard', restaurant_id=restaurant_id)


class RestaurantAddCategory(LoginRequiredView):
    template_name = 'restaurateur/restaurant/category.html'

    def get(self, request, restaurant_id, category_id=None, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id, owner=request.user)

        category = None

        if category_id is not None:
            category = get_object_or_404(Category, pk=category_id, restaurant=restaurant)
            form = RestaurantAddCategoryForm(instance=category)
        else:
            form = RestaurantAddCategoryForm()

        context = {'form': form, 'restaurant': restaurant, 'edit': category_id, 'category': category}
        return render(request, self.template_name, context)

    def post(self, request, restaurant_id, category_id=None, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id, owner=request.user)

        category = None
        if category_id is not None:
            category = get_object_or_404(Category, pk=category_id, restaurant=restaurant)
            form = RestaurantAddCategoryForm(request.POST, request.FILES, instance=category)
        else:
            form = RestaurantAddCategoryForm(request.POST, request.FILES)

        form.instance.restaurant_id = restaurant.id
        if form.is_valid():
            form.save()
            return redirect('restaurant_dashboard', restaurant_id=restaurant_id)

        context = {'form': form, 'restaurant': restaurant, 'edit': category_id, 'category': category}
        return render(request, self.template_name, context)


class RestaurantDeleteCategory(LoginRequiredView):
    template_name = ''

    def get(self, request, restaurant_id, category_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id, owner=request.user)
        category = get_object_or_404(Category, pk=category_id, restaurant=restaurant)

        category.delete()
        return redirect('restaurant_dashboard', restaurant_id=restaurant.id)


class RestaurantAddAddress(LoginRequiredView):
    template_name = 'restaurateur/restaurant/address.html'

    def get(self, request, restaurant_id, address_id=None, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id, owner=request.user)

        address = None

        if address_id is not None:
            address = get_object_or_404(AddressOfRestaurant, pk=address_id, restaurant_id=restaurant_id)
            form = RestaurantAddressForm(instance=address)
        else:
            form = RestaurantAddressForm()

        context = {'restaurant': restaurant, 'form': form, 'edit': address_id, 'address': address}
        return render(request, self.template_name, context)

    def post(self, request, restaurant_id, address_id=None, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id, owner=request.user)

        if address_id is not None:
            address = get_object_or_404(AddressOfRestaurant, pk=address_id, restaurant_id=restaurant_id)
            form = RestaurantAddressForm(request.POST, request.FILES, instance=address)
        else:
            form = RestaurantAddressForm(request.POST, request.FILES)

        form.instance.restaurant_id = restaurant.id

        if form.is_valid():
            form.save()
            return redirect('restaurant_addresses', restaurant_id=restaurant.id)

        context = {'restaurant': restaurant, 'form': form, 'edit': address_id}
        return render(request, self.template_name, context)


class RestaurantDeleteAddress(LoginRequiredView):
    template_name = ''

    def get(self, request, restaurant_id, address_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id, owner=request.user)
        address = get_object_or_404(AddressOfRestaurant, pk=address_id, restaurant=restaurant)

        address.delete()
        return redirect('restaurant_dashboard', restaurant_id=restaurant.id)
