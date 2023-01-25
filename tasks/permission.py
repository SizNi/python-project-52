from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class TaskDeletePermission(PermissionRequiredMixin):

    def has_permission(self):
        return self.get_object().creator == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, _(
            'Задача может быть удалена только ее автором'))
        return redirect('tasks_home')
