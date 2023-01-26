from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from users.manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=20, null=True, unique=True)
    password = models.CharField(max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    @property
    def is_staff(self):
        return self.is_superuser

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
