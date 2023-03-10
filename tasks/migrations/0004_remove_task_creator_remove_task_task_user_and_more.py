# Generated by Django 4.1.5 on 2023-01-26 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_alter_task_labels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_user',
        ),
        migrations.AddField(
            model_name='task',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='executors', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
    ]
