from django.contrib.auth.models import AbstractUser
from django.db import models


class Level(models.Model):
    easy = models.BooleanField(verbose_name='Легкий')
    normal = models.BooleanField(verbose_name='Нормальный')
    hard = models.BooleanField(verbose_name='Сложный')


class CustomUser(AbstractUser):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
