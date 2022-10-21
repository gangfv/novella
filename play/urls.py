from django.urls import path

from .views import LevelOnePages

urlpatterns = [
    path("level_1/", LevelOnePages.as_view(), name="level_1"),
]