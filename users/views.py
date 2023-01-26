from django.shortcuts import render, redirect
from django.views.generic import (TemplateView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )
from users.models import CustomUser
from users.forms import CreateUserForm, UpdateUserForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class IndexView(TemplateView):

    template_name = 'users.users.html'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            template_name='users.html',
            context={
                'users': CustomUser.objects.all().order_by('id'),
                'title': 'Users'
            }
        )


class CreateView(CreateView):

    def get(self, request, *args, **kwargs):
        context = {}
        form = CreateUserForm()
        context['registration_form'] = form
        return render(request, 'create.html', context)

    def post(self, request, *args, **kwargs):
        context = {}
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            form.cleaned_data.get('username')
            form.cleaned_data.get('password1')
            messages.info(request, _('Пользователь успешно зарегистрирован'))
            return redirect(reverse_lazy('login'))
        else:
            context['registration_form'] = form
            return render(request, 'create.html', context)


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):

    def get(self, request, *args, **kwargs):
        current_user = request.user
        user_id = kwargs.get('pk')
        context = {}
        if current_user.id == user_id:
            user = CustomUser.objects.get(id=user_id)
            form = UpdateUserForm(instance=user)
            context['update_form'] = form
            context['pk'] = user_id
            return render(request, 'update.html', context)
        else:
            messages.error(request, _(
                'У вас нет прав для изменения другого пользователя.'))
            return redirect('users_home')

    def post(self, request, *args, **kwargs):
        context = {}
        user_id = kwargs.get('pk')
        user = CustomUser.objects.get(id=user_id)
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, _('Пользователь успешно изменён'))
            return redirect('home')
        else:
            context['update_form'] = form
            context['pk'] = user_id
            return render(request, 'update.html', context)


@method_decorator(login_required, name='dispatch')
class UserDeleteView(DeleteView):

    def get(self, request, *args, **kwargs):
        context = {}
        current_user = request.user
        user_id = kwargs.get('pk')
        if current_user.id == user_id:
            user = CustomUser.objects.get(id=user_id)
            context['user'] = user
            return render(request, 'delete.html', context)
        else:
            messages.error(request, _(
                'У вас нет прав для изменения другого пользователя.'))
            return redirect('users_home')

    def post(self, request, *args, **kwargs):
        current_user = request.user
        user_id = kwargs.get('pk')
        if current_user.id == user_id:
            user = CustomUser.objects.get(id=user_id)
            logout(request)
            user.delete()
            messages.info(request, _('Пользователь успешно удалён'))
            return redirect('users_home')
