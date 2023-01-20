from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from statuses.models import TaskStatus
from statuses.forms import CreateStatusForm, UpdateStatusForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class StatusesView(TemplateView):
    
    def get(self, request, *args, **kwargs):
        context = {}
        return render(
            request,
            template_name = 'statuses.html',
            context = {
                'statuses': TaskStatus.objects.all().order_by('id'),
                'title': 'Statuses'
            }
        )

@method_decorator(login_required, name='dispatch')
class CreateStatusesView(CreateView):
    
    def get(self, request, *args, **kwargs):
        context = {}
        form = CreateStatusForm()
        context['createstatus_form'] = form
        return render(request, 'create_status.html', context)
    
    def post(self, request, *args, **kwargs):
        context = {}
        form = CreateStatusForm(request.POST)
        if form.is_valid():
            status = form.save()
            messages.info(request, _('Статус создан!'))
            return redirect(reverse_lazy('statuses_home'))
        else:
            context['createstatus_form'] = form
            return render(request, 'create_status.html', context)

@method_decorator(login_required, name='dispatch')
class UpdateStatusesView(UpdateView):
    
    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        context = {}
        status = TaskStatus.objects.get(id=status_id)
        form = UpdateStatusForm(instance=status)
        context['updatestatus_form'] = form
        context['pk'] = status_id
        return render(request, 'update_status.html', context) 
    
    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        context = {}
        status = TaskStatus.objects.get(id=status_id)
        form = UpdateStatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.info(request, _('Статус успешно изменён'))
            return redirect('statuses_home')
        else:
            context['updatestatus_form'] = form
            context['pk'] = status_id
            return render(request, 'update_status.html', context)


@method_decorator(login_required, name='dispatch')
class DeleteStatusView(DeleteView):
    
    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        context = {}
        status = TaskStatus.objects.get(id=status_id)
        context['status'] = status
        return render(request, 'delete_status.html', context) 
        
    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        context = {}
        status = TaskStatus.objects.get(id=status_id)
        context['status'] = status
        status.delete()
        messages.info(request, _('Статус удален'))
        return redirect('statuses_home')