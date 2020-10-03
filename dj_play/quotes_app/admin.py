from django.contrib import admin

from quotes_app.models import Quote, Reflection

# Register your models here.

models = [Quote, Reflection]
admin.site.register(models)
