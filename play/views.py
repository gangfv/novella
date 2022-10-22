from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from accounts.models import CustomUser, Products


class LevelOnePages(TemplateView):
    template_name = "pages/level_1.html"


class LessonPage(TemplateView):
    template_name = 'pages/learn.html'


def products_value(request, money, money_sell):
    if money > money_sell:
        CustomUser.objects.update(money=int(money) - money_sell)
    else:
        messages.info(request, 'У вас нет денег!')


def play_money(request, money):
    if money > 0:
        if 'Хлеб 30 руб' in request.POST:
            products_value(request, money, 30)
        elif 'Гречневая крупа 3 кг 150 руб' in request.POST:
            products_value(request, money, 150)
        elif 'Вода 20л 500 руб' in request.POST:
            products_value(request, money, 500)
        elif 'Курица 250 руб' in request.POST:
            products_value(request, money, 250)
        elif 'Конфеты 300 руб' in request.POST:
            products_value(request, money, 300)
        elif 'Шоколад 100 руб' in request.POST:
            products_value(request, money, 100)
        elif 'Зимняя куртка 7000 руб' in request.POST:
            products_value(request, money, 7000)
        elif 'Коллекционные кроссовки Nike 15 000 руб' in request.POST:
            products_value(request, money, 15000)
        elif 'Тёплые сапоги 3000 руб' in request.POST:
            products_value(request, money, 3000)
        elif 'Новогодние носки 200 руб' in request.POST:
            products_value(request, money, 200)
        elif 'Лекарства 1000 руб' in request.POST:
            products_value(request, money, 1000)
        elif 'Тарелки 400 руб' in request.POST:
            products_value(request, money, 400)
        elif 'Кружка с динозавром 500 руб' in request.POST:
            products_value(request, money, 500)
        elif 'Очки Гучи 5000 руб' in request.POST:
            products_value(request, money, 5000)
        elif 'Смарт часы 10000 руб' in request.POST:
            products_value(request, money, 10000)
        elif 'Сигареты 500 руб' in request.POST:
            products_value(request, money, 500)
        elif 'Кольцо 2000 руб' in request.POST:
            products_value(request, money, 2000)
        elif 'Золотая цепь 3000 руб' in request.POST:
            products_value(request, money, 3000)
    else:
        messages.info(request, 'У вас не хватает денег!')


class PlayGame(ListView):
    model = Products
    context_object_name = 'product'
    template_name = 'pages/play_game.html'

    def post(self, request, *args, **kwargs):
        money = [i for i in CustomUser.objects.values('money')][0]['money']
        play_money(request, money)
        return redirect('/play/play_game/')


def InvestEasy(request):
    money = [i for i in CustomUser.objects.values('money')][0]['money']
    level = int([i for i in CustomUser.objects.values('level')][0]['level'])
    if money < 3000:
        return redirect('over_sell')
    elif level == 1:
        if money > 14000:
            return redirect('over_dead')
        else:
            return render(request, 'pages/invest_1.html')
    elif level == 2:
        if money > 9000:
            return redirect('over_dead')
        else:
            return render(request, 'pages/invest_1.html')
    elif level == 3:
        if money > 4000:
            return redirect('over_dead')
        else:
            return render(request, 'pages/invest_1.html')
    else:
        return render(request, 'pages/invest_1.html')


class OverDeadPageView(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = "pages/over_dead.html"
    login_url = 'account_login'

    def post(self, request, *args, **kwargs):
        level = int([i for i in CustomUser.objects.values('level')][0]['level'])
        level_user = int([i for i in request.POST][-1])
        if 1 == level_user:
            CustomUser.objects.update(level_id=1, money=15000, session_user_id=1)
        elif 2 == level_user:
            CustomUser.objects.update(level_id=2, money=10000, session_user_id=1)
        elif 3 == level_user:
            CustomUser.objects.update(level_id=3, money=5000, session_user_id=1)
        return redirect('play_game_products')


class OverSellPageView(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = "pages/over_sell.html"
    login_url = 'account_login'

    def post(self, request, *args, **kwargs):
        level = int([i for i in CustomUser.objects.values('level')][0]['level'])
        level_user = int([i for i in request.POST][-1])
        if 1 == level_user:
            CustomUser.objects.update(level_id=1, money=15000, session_user_id=1)
        elif 2 == level_user:
            CustomUser.objects.update(level_id=2, money=10000, session_user_id=1)
        elif 3 == level_user:
            CustomUser.objects.update(level_id=3, money=5000, session_user_id=1)
        return redirect('play_game_products')
