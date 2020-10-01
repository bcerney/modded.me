from django.urls import path
from quotes_app import views

urlpatterns = [
    path('quotes/', views.quote_list),
    path('quotes/<int:pk>/', views.quote_detail),
]