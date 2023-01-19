from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from users.models import CustomUser
from users.forms import CreateUserForm, UpdateUserForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class StatusesView(TemplateView):
    pass
