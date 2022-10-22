import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from accounts.models import CustomUser, Products


class LevelOnePages(LoginRequiredMixin, TemplateView):
    template_name = "pages/level_1.html"
    login_url = 'account_login'


class LessonPage(LoginRequiredMixin, TemplateView):
    template_name = 'pages/learn.html'
    login_url = 'account_login'


def products_value(request, money, money_sell):
    if money > money_sell:
        CustomUser.objects.update(money=int(money) - money_sell)
    else:
        messages.info(request, 'У вас нет денег!')


def play_money(req, money):
    body = json.loads(req.POST)
    print(body)

    if money >= body.cost:
        print()
    else:
        messages.info(req, 'У вас не хватает денег!')

def getUserMoney(request):

        print("Jrtq")
        money = [i for i in CustomUser.objects.values('money')][0]['money']

        return HttpResponse(json.dumps({'money': money}))

class PlayGame(LoginRequiredMixin, ListView):
    model = Products
    context_object_name = 'product'
    template_name = 'pages/play_game.html'

    def post(self, request, *args, **kwargs):
        money = [i for i in CustomUser.objects.values('money')][0]['money']

        print(money)
        play_money(request, money)
        return redirect('/play/play_game/')


class InvestEasy(LoginRequiredMixin, TemplateView):
    template_name = 'pages/invest_1.html'
    login_url = 'account_login'

    def post(self, request, *args, **kwargs):
        if str(request.POST) != '<QueryDict: {}>':
            money = [i for i in CustomUser.objects.values('money')][0]['money']
            tiket = [i for i in request.POST][-1]
            if 'tiket_1' in tiket:
                CustomUser.objects.update(level_id=1, money=int(money) - 2000, session_user_id=1)
            if 'tiket_2' in tiket:
                CustomUser.objects.update(level_id=1, money=int(money) + 10000, session_user_id=1)
            if 'tiket_3' in tiket:
                CustomUser.objects.update(level_id=1, money=int(money) + 5000, session_user_id=1)
            if 'tiket_4' in tiket:
                CustomUser.objects.update(level_id=1, money=int(money) - 1000, session_user_id=1)
            if 'tiket_5' in tiket:
                CustomUser.objects.update(level_id=1, money=int(money) - 1000, session_user_id=1)
            if 'tiket_6' in tiket:
                CustomUser.objects.update(level_id=1, money=int(money) + 10000, session_user_id=1)
            if 'tiket_7' in tiket:
                CustomUser.objects.update(level_id=1, money=int(money) + 10000, session_user_id=1)
            if 'tiket_8' in tiket:
                CustomUser.objects.update(level_id=1, money=int(money) + 10000, session_user_id=1)
            if 'tiket_9' in tiket:
                CustomUser.objects.update(level_id=1, money=int(money) + 10000, session_user_id=1)
            if 'tiket_10' in tiket:
                CustomUser.objects.update(level_id=1, money=int(money) + 10000, session_user_id=1)

        return redirect('invest_easy')


class OverSellPageView(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = "pages/over_sell.html"
    login_url = 'account_login'

    def post(self, request, *args, **kwargs):
        level_user = int([i for i in request.POST][-1])
        if 1 == level_user:
            CustomUser.objects.update(level_id=1, money=15000, session_user_id=1)
        elif 2 == level_user:
            CustomUser.objects.update(level_id=2, money=10000, session_user_id=1)
        elif 3 == level_user:
            CustomUser.objects.update(level_id=3, money=5000, session_user_id=1)
        return redirect('play_game_products')
