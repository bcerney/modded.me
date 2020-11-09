from django.contrib.auth import views as auth_views
from django.urls import path

# TODO: apply this relative import approach to quotes_api
from . import views

app_name = "quotes_app"
urlpatterns = [
    # quotes/
    path("quotes/", views.HomeView.as_view(), name="home"),
    path("quotes/<int:pk>/", views.QuoteDetailView.as_view(), name="quote-detail"),
    path("quotes/add-quote/", views.QuoteCreateView.as_view(), name="add-quote"),
    # reflections/
    path(
        "reflections/<int:pk>/",
        views.ReflectionDetailView.as_view(),
        name="reflection-detail",
    ),
    path(
        "reflections/add-reflection/<int:quote_id>/",
        views.ReflectionCreateView.as_view(),
        name="add-reflection",
    ),
    # tags
    path("tags/<int:pk>/", views.TagQuoteListView.as_view(), name="tag-quotes"),
]
