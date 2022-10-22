from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView

from accounts.models import CustomUser


class HomePageView(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = "pages/home.html"
    login_url = 'account_signup'

    def post(self, request, *args, **kwargs):
        if 'easy' in request.POST:
            CustomUser.objects.update(level_id=1, money=15000, session_user_id=1)
        elif 'normal' in request.POST:
            CustomUser.objects.update(level_id=2, money=10000, session_user_id=1)
        elif 'hard' in request.POST:
            CustomUser.objects.update(level_id=3, money=5000, session_user_id=1)
        return redirect('/play/level_1')
