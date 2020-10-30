from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    CustomUser,
    Sprint,
    Task,
    Topic,
    UserProfile,
    Virtue,
    SprintVirtueTally,
)

admin.site.register(CustomUser, UserAdmin)

# TODO: need this?
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'virtues']

# admin.site.register(UserProfile, UserProfileAdmin)

models = Sprint, Task, Topic, UserProfile, Virtue, SprintVirtueTally
admin.site.register(models)
