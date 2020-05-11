from ..forms import *
from .base_views import *
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


class Profile(LoginRequiredView):
    template_name = 'account/profile.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        user_id = user.id
        usermodel = get_object_or_404(User, pk=user_id)
        form_edit = UserEditForm(instance=usermodel)
        form_edit_password = None
        change_password = False
        if request.GET.get('change_password'):
            form_edit_password = PasswordChangeForm(user=user, data=request.POST)
            change_password = True

        elif request.GET.get('cancel'):
            change_password = False
        context = {'form_edit': form_edit, 'form_edit_password': form_edit_password, 'user': usermodel,
                   'change_password': change_password}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        user = request.user
        user_id = user.id
        usermodel = get_object_or_404(User, pk=user_id)
        form_edit = UserEditForm(request.POST, instance=usermodel)
        form_edit_password = PasswordChangeForm(user=user, data=request.POST)

        if form_edit.is_valid():
            form_edit.save()
            messages.success(request, 'Профиль обновлён.')
            if form_edit_password.is_valid():
                messages.success(request, 'Пароль обновлён.')
                form_edit_password.save()
                update_session_auth_hash(request, form_edit_password.user)

            else:
                messages.error(request, 'Ошибка ввода пароля.')
                return redirect('profile')
        else:
            messages.error(request, 'Ошибка введённых данных.')

        context = {'form_edit_password': form_edit_password, 'user': usermodel, 'form_edit': form_edit}
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
