from django.contrib.auth.models import AbstractUser
from django.db import models

SESSION = (
    ('1', 'Сессия 1'),
    ('2', 'Сессия 2'),
    ('3', 'Сессия 3'),
    ('4', 'Сессия 4'),
    ('5', 'Сессия 5'),
    ('6', 'Сессия 6'),
    ('7', 'Сессия 7'),
    ('8', 'Сессия 8'),
    ('9', 'Сессия 9'),
    ('10', 'Сессия 10'),
)

LEVELS = (
    ('Легкий', 'Легкий'),
    ('Нормальный', 'Нормальный'),
    ('Сложный', 'Сложный'),
)

PRODUCT = (
    ('Хлеб 30 руб', 'Хлеб 30 руб'),
    ('Гречневая крупа 3 кг 150 руб', 'Гречневая крупа 3 кг 150 руб '),
    ('Вода 20л 500 руб', 'Вода 20л 500 руб'),
    ('Курица 250 руб', 'Курица 250 руб'),
    ('Конфеты 300 руб', 'Конфеты 300 руб'),
    ('Шоколад 100 руб', 'Шоколад 100 руб'),
    ('Зимняя куртка 7000 руб', 'Зимняя куртка 7000 руб'),
    ('Коллекционные кроссовки Nike 15 000 руб', 'Коллекционные кроссовки Nike 15 000 руб'),
    ('Тёплые сапоги 3000 руб', 'Тёплые сапоги 3000 руб'),
    ('Новогодние носки 200 руб', 'Новогодние носки 200 руб'),
    ('Лекарства 1000 руб', 'Лекарства 1000 руб'),
    ('Тарелки 400 руб', 'Тарелки 400 руб'),
    ('Кружка с динозавром 500 руб', 'Кружка с динозавром 500 руб'),
    ('Очки Гучи 5000 руб', 'Очки Гучи 5000 руб'),
    ('Смарт часы 10000 руб', 'Смарт часы 10000 руб'),
    ('Сигареты 500 руб', 'Сигареты 500 руб'),
    ('Кольцо 2000 руб', 'Кольцо 2000 руб'),
    ('Золотая цепь 3000 руб', 'Золотая цепь 3000 руб'),
)


class Session(models.Model):
    sessions_full = models.CharField(choices=SESSION, null=True, max_length=25)

    def __str__(self):
        return self.sessions_full


class Level(models.Model):
    levels_full = models.CharField(choices=LEVELS, null=True, max_length=25)

    def __str__(self):
        return self.levels_full


class Product(models.Model):
    products_full = models.CharField(choices=PRODUCT, null=True, max_length=100)

    def __str__(self):
        return self.products_full


class CustomUser(AbstractUser):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True)
    money = models.IntegerField(default=0)
    session_user = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, blank=True)
    products_user_full = models.ManyToManyField(Product, null=True, blank=True)

    def __str__(self):
        return self.username
