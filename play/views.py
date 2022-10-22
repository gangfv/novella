from django.shortcuts import redirect
from django.views.generic import TemplateView


class LevelOnePages(TemplateView):
    template_name = "pages/level_1.html"

    # def post(self, request, *args, **kwargs):
    #     if 'easy' in request.POST:
    #         print("easy")
    #     elif 'normal' in request.POST:
    #         print("normal")
    #     elif 'hard' in request.POST:
    #         print("hard")
    #     return redirect('/')


class LessonPage(TemplateView):
    template_name = 'pages/learn.html'


class PlayGame(TemplateView):
    template_name = 'pages/play_game.html'
