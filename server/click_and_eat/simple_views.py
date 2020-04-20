from django.shortcuts import render
from .models import *

# Create your views here.


def restaurant_map(request):
    if request.user.is_authenticated:
        context = {'restaurants': Restaurant.objects.all()}
        return render(request, 'maps/rest_map.html', context)
    else:
        return render(request, 'welcome.html')
