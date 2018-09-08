from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .models import Map, UsersMaps, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
# admin.site.register(User)
admin.site.register(Map)
admin.site.register(UsersMaps)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(CustomUser, CustomUserAdmin)
