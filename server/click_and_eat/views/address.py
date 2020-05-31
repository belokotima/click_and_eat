from ..forms import *
from .base_views import *
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404


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
            return redirect('restaurant_dashboard', restaurant_id=restaurant.id)

        context = {'restaurant': restaurant, 'form': form, 'edit': address_id}
        return render(request, self.template_name, context)


class RestaurantDeleteAddress(LoginRequiredView):
    template_name = ''

    def get(self, request, restaurant_id, address_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id, owner=request.user)
        address = get_object_or_404(AddressOfRestaurant, pk=address_id, restaurant=restaurant)

        address.delete()
        return redirect('restaurant_dashboard', restaurant_id=restaurant.id)


class RestaurantAddressDashboard(LoginRequiredView):
    template_name = 'restaurateur/restaurant/address/dashboard.html'

    def get(self, request, restaurant_id, address_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id, owner=request.user)
        address = get_object_or_404(AddressOfRestaurant, pk=address_id, restaurant=restaurant)

        context = {'restaurant': restaurant, 'address': address}
        return render(request, self.template_name, context)


class RestaurantAddressOrdersContents(LoginRequiredView):
    template_name = 'restaurateur/restaurant/address/base/orders.html'

    def get(self, request, restaurant_id, address_id, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id, owner=request.user)
        address = get_object_or_404(AddressOfRestaurant, pk=address_id, restaurant=restaurant)

        context = {'restaurant': restaurant, 'address': address}
        return render(request, self.template_name, context)


class RestaurantAddressOrder(LoginRequiredView):
    template_name = 'restaurateur/restaurant/address/order.html'

    def get(self, request, address_id, order_id, *args, **kwargs):
        address = get_object_or_404(AddressOfRestaurant, restaurant__owner=request.user, id=address_id)
        restaurant = address.restaurant
        order = get_object_or_404(Order, restaurant=address, id=order_id)
        form = OrderFinishForm()
        context = {'restaurant': restaurant, 'address': address, 'order': order, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, address_id, order_id, *args, **kwargs):
        address = get_object_or_404(AddressOfRestaurant, restaurant__owner=request.user, id=address_id)
        restaurant = address.restaurant
        order = get_object_or_404(Order, restaurant=address, id=order_id)
        form = OrderFinishForm(request.POST)

        if form.is_valid():
            if order.secret_code == str(form.cleaned_data['secret_code']):
                order.clear_status()
                order.finished = True
                order.save()
                return redirect('restaurant_address_dashboard', restaurant_id=restaurant.id, address_id=address_id)

        context = {'restaurant': restaurant, 'address': address, 'order': order, 'form': form}
        return render(request, self.template_name, context)


class RestaurantAddressOrderContents(LoginRequiredView):
    template_name = 'main/base/order_base.html'

    def get(self, request, restaurant_id, address_id, order_id, *args, **kwargs):
        address = get_object_or_404(AddressOfRestaurant, restaurant__owner=request.user, id=address_id)
        restaurant = address.restaurant
        order = get_object_or_404(Order, id=order_id, restaurant=address)
        context = {'restaurant': order.restaurant.restaurant, 'address': address, 'order': order}
        return render(request, self.template_name, context)


class RestaurantAddressOrderInProgress(LoginRequiredView):

    def get(self, request, address_id, order_id, *args, **kwargs):
        address = get_object_or_404(AddressOfRestaurant, restaurant__owner=request.user, id=address_id)
        restaurant = address.restaurant
        order = get_object_or_404(Order, restaurant=address, id=order_id)
        order.clear_status()
        order.in_progress = True
        order.save()
        return redirect('restaurant_address_order', restaurant_id=restaurant.id, address_id=address_id,
                        order_id=order_id)


class RestaurantAddressOrderCancel(LoginRequiredView):

    def post(self, request, address_id, order_id, *args, **kwargs):
        reason = request.POST.get('cancel_reason', None)
        address = get_object_or_404(AddressOfRestaurant, restaurant__owner=request.user, id=address_id)
        restaurant = address.restaurant
        order = get_object_or_404(Order, restaurant=address, id=order_id)
        order.clear_status()
        order.canceled = True
        order.cancel_reason = reason
        order.save()
        return redirect('restaurant_address_order', restaurant_id=restaurant.id, address_id=address_id,
                        order_id=order_id)


class RestaurantAddressOrderReady(LoginRequiredView):

    def get(self, request, address_id, order_id, *args, **kwargs):
        address = get_object_or_404(AddressOfRestaurant, restaurant__owner=request.user, id=address_id)
        restaurant = address.restaurant
        order = get_object_or_404(Order, restaurant=address, id=order_id)
        order.clear_status()
        order.ready = True
        order.save()
        return redirect('restaurant_address_order', restaurant_id=restaurant.id, address_id=address_id,
                        order_id=order_id)


class RestaurantAddressOrdersMonitor(LoginRequiredView):
    template_name = 'restaurateur/restaurant/address/orders_monitor.html'

    def get(self, request, address_id, *args, **kwargs):
        address = get_object_or_404(AddressOfRestaurant, restaurant__owner=request.user, id=address_id)
        restaurant = address.restaurant
        all_orders = address.get_last_orders()
        orders = all_orders.filter(ready=False, in_progress=True)
        ready_orders = all_orders.filter(ready=True)
        context = {'restaurant': restaurant, 'address': address, 'orders': orders, 'ready_orders': ready_orders}
        return render(request, self.template_name, context)


class RestaurantAddressOrdersMonitorContents(LoginRequiredView):
    template_name = 'restaurateur/restaurant/address/base/orders_monitor_contents.html'

    def get(self, request, address_id, *args, **kwargs):
        address = get_object_or_404(AddressOfRestaurant, restaurant__owner=request.user, id=address_id)
        restaurant = address.restaurant
        all_orders = address.get_last_orders()
        orders = all_orders.filter(ready=False, in_progress=True)
        ready_orders = all_orders.filter(ready=True)
        context = {'restaurant': restaurant, 'address': address, 'orders': orders, 'ready_orders': ready_orders}
        return render(request, self.template_name, context)
