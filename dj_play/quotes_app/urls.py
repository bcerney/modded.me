from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from quotes_app import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('quotes/', views.QuoteList.as_view()),
    path('quotes/<int:pk>/', views.QuoteDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
