from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone

class Task(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('Name'), blank=False)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    created_date = models.DateTimeField(verbose_name=_("Created date"),
                                        default=timezone.now)
    task_user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default='',
        related_name='task_users',
        verbose_name=_('Task_user')
    )
    creator = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT,
        blank=False,
        default='',
        related_name='creator',
        verbose_name=_('Creator')
    )
    status = models.ForeignKey(
        to='statuses.TaskStatus',
        on_delete=models.PROTECT,
        blank=False,
        default='',
        related_name='statuses',
        verbose_name=_('Status')
    )
    
    def __str__(self):
        return self.name
