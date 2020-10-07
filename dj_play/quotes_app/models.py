from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager


class Quote(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    # TODO: https://stackoverflow.com/questions/2886987/adding-custom-fields-to-users-in-django
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="quotes", on_delete=models.CASCADE
    )
    text = models.TextField()
    author = models.CharField(max_length=200, blank=True, default="")
    tags = TaggableManager()

    def __str__(self):
        return f'"{self.text}" - {self.author}'

    def get_absolute_url(self):
        return reverse("quotes_app:quote-detail", args=[self.id])

    class Meta:
        ordering = ["created"]


class Reflection(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="reflections", on_delete=models.CASCADE
    )
    quote = models.ForeignKey(
        "Quote", related_name="reflections", on_delete=models.CASCADE
    )
    # TODO: confirm attributes of TextField, good fit?
    text = models.TextField()

    def __str__(self):
        return f"{self.created} | {self.text}"

    def get_absolute_url(self):
        return reverse("quotes_app:reflection-detail", args=[self.id])

    class Meta:
        ordering = ["created"]


# https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
class User(AbstractUser):
    pass
