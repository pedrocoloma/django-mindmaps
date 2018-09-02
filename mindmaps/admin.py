from django.contrib import admin

from .models import User, Map, UsersMaps

# Register your models here.
admin.site.register(User)
admin.site.register(Map)
admin.site.register(UsersMaps)
