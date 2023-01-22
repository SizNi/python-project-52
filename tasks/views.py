from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django_filters.views import FilterView
from tasks.models import Task
from statuses.models import TaskStatus
from users.models import CustomUser
from tasks.filters import TasksFilterForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from urllib import request


@method_decorator(login_required, name='dispatch')
class TasksView(FilterView):
    model = Task
    filterset_class = TasksFilterForm
    template_name = 'tasks.html'
    context_object_name = "tasks"
    extra_context = {'title': _('Tasks')}