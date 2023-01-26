from django import forms
from django_filters import FilterSet, BooleanFilter
from django.utils.translation import gettext_lazy as _
from tasks.models import Task


class TasksFilterForm(FilterSet):
    only_user = BooleanFilter(
        label=_('Только свои задачи'),
        widget=forms.CheckboxInput(),
        method='only_self',
        field_name='only_self_tasks'
    )

    def only_self(self, queryset, name, value):
        result = queryset.filter(author=self.request.user)
        if value:
            return result
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
