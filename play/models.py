from django.db import models


class Point(models.Model):
    money = models.IntegerField(default=500)
