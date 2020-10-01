from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from quotes_app import views

urlpatterns = [
    path('quotes/', views.quote_list),
    path('quotes/<int:pk>/', views.quote_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
