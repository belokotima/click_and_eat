from ..forms import *
from .base_views import *
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404


class Profile(LoginRequiredView):
    template_name = 'account/profile.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        user_id = user.id
        usermodel = get_object_or_404(User, pk=user_id)
        form = UserEditForm(instance=usermodel)
        context = {'form': form, 'user': usermodel}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = request.user
        user_id = user.id
        usermodel = get_object_or_404(User, pk=user_id)
        form = UserEditForm(request.POST, instance=usermodel)
        form.instance.username = user

        if form.is_valid():
            if form.repeat_password == form.instance.password:
                form.save()
                return redirect('profile')
        context = {'form': form, 'user': usermodel, 'edit': True}
        return render(request, self.template_name, context)


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
