from django.contrib import admin

from quotes_app.models import Quote, Reflection


models = [Quote, Reflection]
admin.site.register(models)