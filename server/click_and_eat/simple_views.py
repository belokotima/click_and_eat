from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from .views.cart import *


# Create your views here.


def restaurant_map(request):
    if request.user.is_authenticated:
        context = {'restaurants': Restaurant.objects.all()}
        return render(request, 'maps/rest_map.html', context)
    else:
        return render(request, 'welcome.html')


def restaurants_map_data(request):
    restaurant_id = request.GET.get('restaurant_id', None)

    selected_address_id = None

    if restaurant_id is None:
        restaurants = Restaurant.objects.all()
    else:
        cart = Cart.load(request)
        selected_address_id = cart.address_id
        restaurants = [Restaurant.objects.get(id=restaurant_id), ]

    restaurants_list = []

    for restaurant in restaurants:
        addresses_list = []

        for address in restaurant.get_addresses():
            addresses_list.append(
                {'id': address.id, 'lon': address.longitude, 'lat': address.latitude, 'address': address.address})

        restaurants_list.append(
            {'logo': restaurant.logo.url, 'title': restaurant.title, 'description': restaurant.description,
             'open_time': restaurant.open_time.strftime('%H:%M'),
             'close_time': restaurant.close_time.strftime('%H:%M'), 'addresses': addresses_list})

    return JsonResponse({'restaurants': restaurants_list, 'selected_address_id': selected_address_id})
