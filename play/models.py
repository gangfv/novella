from django.db import models


class Level(models.Model):
    first = models.BooleanField(default=False)
    second = models.BooleanField(default=False)
    third = models.BooleanField(default=False)


class Side(models.Model): # побочка
    first = models.BooleanField(default=False)
    second = models.BooleanField(default=False)
    third = models.BooleanField(default=False)


class Point(models.Model):
    money = models.IntegerField(default=0)
