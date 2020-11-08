from django.contrib import admin

from .models import Journal, JournalEntry, MannaProfile

models = [MannaProfile, Journal, JournalEntry]
admin.site.register(models)
