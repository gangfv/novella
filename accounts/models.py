from django.contrib.auth.models import AbstractUser
from django.db import models


class Session(models.Model):
    session_one = models.BooleanField()
    session_two = models.BooleanField()
    session_three = models.BooleanField()
    session_four = models.BooleanField()
    session_five = models.BooleanField()
    session_six = models.BooleanField()
    session_seven = models.BooleanField()
    session_eight = models.BooleanField()
    session_nine = models.BooleanField()
    session_ten = models.BooleanField()


class Level(models.Model):
    easy = models.BooleanField(verbose_name='Легкий')
    normal = models.BooleanField(verbose_name='Нормальный')
    hard = models.BooleanField(verbose_name='Сложный')


class CustomUser(AbstractUser):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True)
    money = models.IntegerField(default=40000)
    session_user = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username
