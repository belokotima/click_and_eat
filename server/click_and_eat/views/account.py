from ..forms import *
from .base_views import *
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


class ProfileView(LoginRequiredView):
    template_name = 'account/profile.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        user_id = user.id
        usermodel = get_object_or_404(User, pk=user_id)
        form_edit = UserEditForm(instance=usermodel)

        context = {'form_edit': form_edit, 'user': usermodel}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        user = request.user
        user_id = user.id
        usermodel = get_object_or_404(User, pk=user_id)
        form_edit = UserEditForm(request.POST, instance=usermodel)

        if form_edit.is_valid():
            form_edit.save()
            messages.success(request, 'Профиль обновлён.')
        else:
            messages.error(request, '')

        context = {'user': usermodel, 'form_edit': form_edit}
        return render(request, self.template_name, context)


class PasswordChange(LoginRequiredView):
    template_name = 'account/password_change.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        user_id = user.id
        usermodel = get_object_or_404(User, pk=user_id)
        form_edit_password = PasswordChangeForm(user=user, data=request.POST)

        context = {'form_edit_password': form_edit_password, 'user': usermodel}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        user = request.user
        user_id = user.id
        usermodel = get_object_or_404(User, pk=user_id)
        form_edit_password = PasswordChangeForm(user=user, data=request.POST)
        if form_edit_password.is_valid():
            form_edit_password.save()
            update_session_auth_hash(request, form_edit_password.user)
            messages.success(request, 'Пароль обновлён.')
            return redirect('profile')

        context = {'form_edit_password': form_edit_password, 'user': usermodel}
        return render(request, self.template_name, context)


class History(LoginRequiredView):
    template_name = 'account/history.html'

    def get(self, request):
        context = {'orders': Order.objects.filter(customer=request.user).order_by('-order_time')}
        return render(request, self.template_name, context)


class Habits(LoginRequiredView):
    template_name = 'account/habits.html'

    def get(self, request):
        return render(request, self.template_name)


class Settings(LoginRequiredView):
    template_name = 'account/settings.html'

    def get(self, request):
        return render(request, self.template_name)


class Allergy(LoginRequiredView):
    template_name = 'account/allergy.html'

    def get(self, request):
        return render(request, self.template_name)
