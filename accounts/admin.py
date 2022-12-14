from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Level, Session, Products


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'level', 'money', 'session_user', ]
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'level', 'money', 'session_user',)
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Level)
admin.site.register(Session)
admin.site.register(Products)
