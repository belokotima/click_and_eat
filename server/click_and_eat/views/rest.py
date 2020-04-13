import os
from django import forms
from django.views import View
from django.shortcuts import render, redirect


class RestaurantRegister(View):
    template_name = 'rest/register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
