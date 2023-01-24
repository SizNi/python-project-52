from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from tasks.models import Task
from tasks.filters import TasksFilterForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from urllib import request
from tasks.permission import TaskDeletePermission


@method_decorator(login_required, name='dispatch')
class LabelsView(ListView):
    pass
