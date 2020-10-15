from django.urls import path, include

from . import views


app_name = "get_lucky_draw"
urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
]
