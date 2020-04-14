import os
from ..forms import *
from django.views import View
from django.shortcuts import render, redirect


class RestaurantRegister(View):
    template_name = 'rest/register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RestaurantMenu(View):
    template_name = 'rest/menu.html'

    def get(self, request, *args, **kwargs):
        form = RestaurantMenuForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RestaurantMenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, self.template_name)
