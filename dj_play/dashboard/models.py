from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save


# https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
class CustomUser(AbstractUser):
    pass


class UserProfile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return f"{self.user} Profile"

    class Meta:
        ordering = ["created"]

# TODO: move to signals.py file
# https://blog.khophi.co/extending-django-user-model-userprofile-like-a-pro/
def create_user_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()

post_save.connect(create_user_profile, sender=CustomUser)

class Virtue(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_profile = models.ForeignKey(
        "UserProfile",
        related_name="virtues",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200, blank=False)
    level = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)
    next_level_xp = models.IntegerField()
    # topics = models.ForeignKey(
    #     "Topic",
    #     related_name="virtue",
    #     blank=True,
    #     on_delete=models.CASCADE,
    # )
    # tasks = models.ForeignKey(
    #     "Task",
    #     related_name="virtue",
    #     blank=True,
    #     on_delete=models.CASCADE,
    # )

    def __str__(self):
        return f"{self.title} | Level {self.level}"

    class Meta:
        ordering = ["level"]

class Topic(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200, blank=False)
    virtue = models.ForeignKey(
        "Virtue",
        related_name="topics",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["created"]

class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200, blank=False)
    notes = models.TextField(null=True, blank=True)
    xp = models.IntegerField(default=1)
    virtue = models.ForeignKey(
        "Virtue",
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    topic = models.ForeignKey(
        "Topic",
        related_name="tasks",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.title} | {self.xp} XP"

    class Meta:
        ordering = ["created"]
