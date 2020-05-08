from ..forms import *
from .base_views import *
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404


class Profile(View):
    template_name = 'account/profile.html'

    def get(self, request):
        return render(request, self.template_name)


class History(View):
    template_name = 'account/history.html'

    def get(self, request):
        return render(request, self.template_name)


class Habits(View):
    template_name = 'account/habits.html'

    def get(self, request):
        return render(request, self.template_name)


class Settings(View):
    template_name = 'account/settings.html'

    def get(self, request):
        return render(request, self.template_name)


class Allergy(View):
    template_name = 'account/allergy.html'

    def get(self, request):
        return render(request, self.template_name)
