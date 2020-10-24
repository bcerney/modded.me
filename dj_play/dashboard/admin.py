from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Task, Topic, UserProfile, Virtue

admin.site.register(CustomUser, UserAdmin)

# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'virtues']

# admin.site.register(UserProfile, UserProfileAdmin)

models = UserProfile, Task, Topic, Virtue
admin.site.register(models)
