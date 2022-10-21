from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Level


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'level', 'money']
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password', 'level', 'money')
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Level)
