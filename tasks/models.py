from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone


class Task(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('Имя'), blank=False)
    description = models.TextField(verbose_name=_('Описание'), blank=True)
    created_date = models.DateTimeField(verbose_name=_("Created date"),
                                        default=timezone.now)
    task_user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default='',
        related_name='task_users',
        verbose_name=_('Исполнитель')
    )
    creator = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT,
        blank=False,
        default='',
        related_name='creator',
        verbose_name=_('Автор')
    )
    status = models.ForeignKey(
        to='statuses.TaskStatus',
        on_delete=models.PROTECT,
        blank=False,
        default='',
        related_name='statuses',
        verbose_name=_('Статус')
    )
    labels = models.ManyToManyField(
        'labels.Labels', through='TaskLabelRel',
        through_fields=('task', 'label'), blank=True,
        related_name='tasks', verbose_name=_('Метки'),
    )

    def __str__(self):
        return self.name


class TaskLabelRel(models.Model):
    task = models.ForeignKey(to='tasks.Task', on_delete=models.CASCADE)
    label = models.ForeignKey(to='labels.Labels', on_delete=models.PROTECT)
