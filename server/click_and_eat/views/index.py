import os
from django import forms
from django.views import View
from django.shortcuts import render, redirect


class Index(View):
    template_name = 'welcome.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'main/index.html')
        else:
            return render(request, self.template_name)
