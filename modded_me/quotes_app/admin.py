from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from quotes_app.models import Quote, Reflection


models = [Quote, Reflection]
admin.site.register(models)
