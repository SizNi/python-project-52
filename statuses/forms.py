from django import forms
from django.utils.translation import gettext as _
from statuses.models import TaskStatus


class CreateStatusForm(forms.ModelForm):
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


class UpdateStatusForm(forms.ModelForm):
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
