from django.urls import path, include

from . import views


app_name = "dashboard"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
]
