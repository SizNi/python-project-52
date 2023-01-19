from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from statuses.models import TaskStatus


class CreateStatusForm(UserCreationForm):
    name = forms.CharField(label=_('Имя'),
                                 label_suffix='',
                                 max_length=120,
                                 required=True,
                                 widget=forms.TextInput(
        attrs={'placeholder': _('Имя статуса'),
               'class': 'form-control', }))

    class Meta:
        model = TaskStatus
        fields = ('name',)
