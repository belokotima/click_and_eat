from ..forms import *
from .base_views import *
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404


class Profile(View):
    template_name = 'profile/profile.html'

    def get(self, request):
        return render(request, self.template_name)
