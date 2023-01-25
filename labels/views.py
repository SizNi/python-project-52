from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from labels.models import Labels


@method_decorator(login_required, name='dispatch')
class LabelsView(ListView):
    model = Labels
    template_name = 'labels.html'
    context_object_name = "labels"
    extra_context = {'title': _('labels')}


@method_decorator(login_required, name='dispatch')
class LabelCreateView(SuccessMessageMixin, CreateView):
    model = Labels
    fields = ['name']
    template_name = 'label_create.html'
    context_object_name = "labels"
    success_url = reverse_lazy('labels_home')
    success_message = _('Метка успешно создана')
    extra_context = {'title': _('Создать метку'),
                     'btn': _('Создать'),
                     }


@method_decorator(login_required, name='dispatch')
class LabelUpdateView(SuccessMessageMixin, UpdateView):
    model = Labels
    fields = ['name']
    template_name = 'label_create.html'
    context_object_name = "labels"
    success_url = reverse_lazy('labels_home')
    success_message = _('Метка успешно изменена')
    extra_context = {'title': _('Изменение метки'),
                     'btn': _('изменить'),
                     }


@method_decorator(login_required, name='dispatch')
class LabelDeleteView(SuccessMessageMixin, DeleteView):
    model = Labels
    template_name = 'label_delete.html'
    context_object_name = "labels"
    success_url = reverse_lazy('labels_home')
    success_message = _('Метка успешно удалена')
    extra_context = {'title': _('Удаление метки'),
                     'btn': _('Да, удалить'),
                     }

    def post(self, request, *args, **kwargs):
        if self.get_object().tasks.count():
            messages.error(
                self.request,
                _('Невозможно удалить метку, потому что она используется')
            )
            return redirect(self.success_url)
        return super().post(self, request, *args, **kwargs)
