import math

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse


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
    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)
    xp_to_next_level = models.IntegerField(default=3)
    xp_to_next_level_constant = models.FloatField(default=3.0)
    level_up_xp_modifier = models.FloatField(default=0.05)

    def __str__(self):
        return f"{self.title} | Level {self.level}"

    def get_absolute_url(self):
        return reverse("dashboard:virtue-detail", args=[self.id])

    def add_task_xp(self, task):
        # If adding XP does not increase level
        if task.xp < self.xp_to_next_level:
            self.xp += task.xp
            self.xp_to_next_level -= task.xp

        elif task.xp >= self.xp_to_next_level:
            task_xp = task.xp

            while task_xp >= self.xp_to_next_level:
                # Increase Virtue level
                self.level += 1

                # Add xp_to_next_level to total xp
                self.xp += self.xp_to_next_level
                task_xp -= self.xp_to_next_level

                # Increase xp_to_next_level_constant by modifier %
                self.xp_to_next_level_constant = self.xp_to_next_level_constant + (
                    self.xp_to_next_level_constant * self.level_up_xp_modifier
                )

                self.xp_to_next_level = int(math.ceil(self.xp_to_next_level_constant))

            # Account for task_xp remainder
            self.xp += task_xp
            self.xp_to_next_level -= task_xp
            return f"{self.user_profile.user.username} reached Level {self.level} in {self.title}!"

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

    def get_absolute_url(self):
        return reverse("dashboard:topic-detail", args=[self.id])

    class Meta:
        ordering = ["created"]


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200, blank=False)
    notes = models.TextField(null=True, blank=True)
    xp = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
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

    def get_absolute_url(self):
        return reverse("dashboard:task-detail", args=[self.id])

    class Meta:
        ordering = ["created"]
