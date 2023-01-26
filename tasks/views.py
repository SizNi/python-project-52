from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from tasks.models import Task
from tasks.filters import TasksFilterForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from tasks.permission import TaskDeletePermission
from users.models import CustomUser


@method_decorator(login_required, name='dispatch')
class TasksView(FilterView):
    model = Task
    filterset_class = TasksFilterForm
    template_name = 'tasks.html'
    context_object_name = "tasks"
    extra_context = {'title': _('Tasks')}


@method_decorator(login_required, name='dispatch')
class TasksCreateView(SuccessMessageMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor', 'labels']
    template_name = 'task_create.html'
    context_object_name = "tasks"
    success_url = reverse_lazy('tasks_home')
    success_message = _('Задача успешно создана')
    extra_context = {
        'title': _('Создание задачи'),
        'btn': _('Создать'),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['executor_opt'] = CustomUser.objects.all()
        return context

    def form_valid(self, form):
        print(type(form))
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class TasksUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor', 'labels']
    template_name = 'task_create.html'
    context_object_name = "tasks"
    success_url = reverse_lazy('tasks_home')
    success_message = _('Задача успешно обновлена')
    extra_context = {'title': _('Обновление задачи'),
                     'btn': _('обновить'),
                     }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['executor_opt'] = CustomUser.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class TasksDeleteView(TaskDeletePermission, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    context_object_name = "tasks"
    success_url = reverse_lazy('tasks_home')
    success_message = _('Задача успешно удалена')
    extra_context = {'title': _('Удаление задачи'),
                     'btn': _('Да, удалить'),
                     }
    permission_required = 'task.author'


class TaskView(DetailView):
    model = Task
    template_name = 'task.html'
    context_object_name = "task"
    extra_context = {'title': _('Просмотр задачи'),
                     }
