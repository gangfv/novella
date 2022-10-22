from django.urls import path

from . import views
from .views import LevelOnePages, LessonPage, PlayGame, InvestEasy, OverSellPageView, getUserMoney

urlpatterns = [
    path("level_1/", LevelOnePages.as_view(), name="level_1"),
    path("lesson_page/", LessonPage.as_view(), name='lesson_page'),
    path("play_game/", PlayGame.as_view(), name="play_game_products"),
    path("play_game/money", getUserMoney),
    path("invest_easy/", InvestEasy.as_view(), name='invest_easy'),
    path("over_sell/", OverSellPageView.as_view(), name='over_sell'),
]