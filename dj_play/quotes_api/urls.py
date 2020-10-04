from django.urls import include, path
from rest_framework.routers import DefaultRouter

from quotes_api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'quotes', views.QuoteViewSet)
router.register(r'reflections', views.ReflectionViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
