import os
from django import forms
from django.views import View
from django.shortcuts import render, redirect

from ..models import *


class Index(View):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        context = {'restaurants': Restaurant.objects.all()}
        return render(request, self.template_name, context)

