from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from tasks.models import Task

class FilterTasksForm(forms.ModelForm):
    
    nickname = forms.CharField(label=_('Имя пользователя'),
                            max_length=20,
                            label_suffix='',
                            required=True,
                            help_text=_('Введите логин'),
                            widget=forms.TextInput(
    attrs={'placeholder': _('Имя пользователя'),
            'autofocus': True,
            'class': 'form-control', }),
    error_messages={'unique': _(
        'Пользователь с таким именем'
        ' уже есть')})
    password = forms.CharField(label=_('Пароль'),
                        label_suffix='',
                        max_length=100,
                        required=True,
                        help_text=_("введите пароль"),
                        widget=forms.PasswordInput(
                        attrs={'placeholder': _('Пароль'),
                            'class': 'form-control', }))
    
    class Meta:
        model = get_user_model()
        fields = ('nickname', 'password')
        
    def clean(self):
        if self.is_valid():
            nickname = self.cleaned_data['nickname']
            password = self.cleaned_data['password']
            if not authenticate(nickname=nickname, password=password):
                raise forms.ValidationError('Неверное имя пользователя или пароль')