from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(label=_('Имя'),
                                 label_suffix='',
                                 max_length=100,
                                 required=True,
                                 widget=forms.TextInput(
        attrs={'placeholder': _('Имя'),
               'class': 'form-control', }))
    last_name = forms.CharField(label=_('Фамилия'),
                                label_suffix='',
                                max_length=100,
                                required=True,
                                widget=forms.TextInput(
                                attrs={'placeholder': _('Фамилия'),
                                       'class': 'form-control', }))
    username = forms.CharField(label=_('Имя пользователя'),
                               max_length=20,
                               label_suffix='',
                               required=True,
                               help_text=_('Обязательное поле. '
                                           'Не более 20 символов.'),
                               widget=forms.TextInput(
        attrs={'placeholder': _('Имя пользователя'),
               'autofocus': True,
               'class': 'form-control', }),
        error_messages={'unique': _(
            'Пользователь с таким именем'
            ' уже есть')})
    password1 = forms.CharField(label=_('Пароль'),
                                label_suffix='',
                                max_length=100,
                                required=True,
                                help_text=_(
                                "Ваш пароль должен содержать "
                                "как минимум 3 символа."),
                                widget=forms.PasswordInput(
                                attrs={'placeholder': _('Пароль'),
                                       'class': 'form-control', }))
    password2 = forms.CharField(label=_('Подтверждение пароля'),
                                label_suffix='',
                                max_length=100,
                                required=True,
                                help_text=_("Для подтверждения введите,"
                                            " пожалуйста, пароль ещё раз."),
                                widget=forms.PasswordInput(
                                    attrs={
                                        'placeholder': _('Подтверждение '
                                                         'пароля'),
                                        'class': 'form-control', }))

    class Meta:
        model = get_user_model()
        fields = (
            'first_name', 'last_name', 'username', 'password1', 'password2'
        )


class UpdateUserForm(UserCreationForm):
    first_name = forms.CharField(label=_('Имя'),
                                 label_suffix='',
                                 max_length=100,
                                 widget=forms.TextInput(
        attrs={'placeholder': _('Имя'),
               'class': 'form-control', }))
    last_name = forms.CharField(label=_('Фамилия'),
                                label_suffix='',
                                max_length=100,
                                widget=forms.TextInput(
                                attrs={'placeholder': _('Фамилия'),
                                       'class': 'form-control', }))
    username = forms.CharField(label=_('Имя пользователя'),
                               max_length=20,
                               label_suffix='',
                               help_text=_('Не более 20 символов.'),
                               widget=forms.TextInput(
        attrs={'placeholder': _('Имя пользователя'),
               'autofocus': True,
               'class': 'form-control', }),
        error_messages={'unique': _(
            'Пользователь с таким именем'
            ' уже есть')})
    password1 = forms.CharField(label=_('Пароль'),
                                label_suffix='',
                                max_length=100,
                                help_text=_(
                                "Ваш пароль должен содержать "
                                "как минимум 3 символа."),
                                widget=forms.PasswordInput(
                                attrs={'placeholder': _('Пароль'),
                                       'class': 'form-control', }))
    password2 = forms.CharField(label=_('Подтверждение пароля'),
                                label_suffix='',
                                max_length=100,
                                help_text=_("Для подтверждения введите,"
                                            " пожалуйста, пароль ещё раз."),
                                widget=forms.PasswordInput(
                                    attrs={
                                        'placeholder': _('Подтверждение '
                                                         'пароля'),
                                        'class': 'form-control', }))

    class Meta:
        model = get_user_model()
        fields = (
            'first_name', 'last_name', 'username', 'password1', 'password2'
        )
