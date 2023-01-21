from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from tasks.models import Task
from statuses.forms import CreateStatusForm, UpdateStatusForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class TasksView(TemplateView):
    
    def get(self, request, *args, **kwargs):
        context = {}
        return render(
            request,
            template_name = 'tasks.html',
            context = {
                'tasks': Task.objects.all().order_by('id'),
                'title': 'Tasks'
            }
        )