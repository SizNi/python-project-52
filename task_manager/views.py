from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from task_manager.forms import LoginUserForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class Index(TemplateView):
    
    template_name = 'index.html'

class LoginView(TemplateView):
    
    def get(self, request, *args, **kwargs):
        context = {}
        form = LoginUserForm()
        context['login_form'] = form
        return render(request, 'login.html', context)
    
    def post(self, request, *args, **kwargs):
        context = {}
        form = LoginUserForm(request.POST)
        
        if form.is_valid():
            nickname = request.POST['nickname']
            password = request.POST['password']
            user = authenticate(nickname = nickname, password = password)
            
            if user:
                login(request, user)
                messages.info(request, _('Вход произведен!'))
                return redirect('home')
        messages.error(request, _('Неверное имя пользователя или пароль.'))
        context['login_form'] = form
        return render(request, 'login.html', context)

class LogoutView(TemplateView):
    
    def get(self, request, *args, **kwargs):
        messages.info(request, _('Успешно вышли!'))
        logout(request)
        return redirect('home')

