from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Labels(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('Имя'))
    created_date = models.DateTimeField(verbose_name=_("Created date"),
                                        default=timezone.now)

    def __str__(self):
        return self.name
