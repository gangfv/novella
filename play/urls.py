from django.urls import path

from .views import LevelOnePages, LessonPage, PlayGame

urlpatterns = [
    path("level_1/", LevelOnePages.as_view(), name="level_1"),
    path("lesson_page/", LessonPage.as_view(), name='lesson_page'),
    path("play_game/", PlayGame.as_view(), name="play_game_products"),
]