from django.urls import path

from . import views
from .views import LevelOnePages, LessonPage, PlayGame, InvestEasy, OverDeadPageView, OverSellPageView

urlpatterns = [
    path("level_1/", LevelOnePages.as_view(), name="level_1"),
    path("lesson_page/", LessonPage.as_view(), name='lesson_page'),
    path("play_game/", PlayGame.as_view(), name="play_game_products"),
    path("invest_easy/", views.InvestEasy, name='invest_easy'),
    path("over_dead/", OverDeadPageView.as_view(), name='over_dead'),
    path("over_sell/", OverSellPageView.as_view(), name='over_sell'),
]