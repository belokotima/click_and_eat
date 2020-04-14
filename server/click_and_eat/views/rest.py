import os
from ..forms import *
from .base_views import *
from django.views import View
from django.shortcuts import render, redirect


class RestaurantRegister(LoginRequiredView):
    template_name = 'rest/register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RestaurantCreate(LoginRequiredView):
    template_name = 'rest/menu.html'

    def get(self, request, *args, **kwargs):
        form = RestaurantEditForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RestaurantEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, self.template_name)
