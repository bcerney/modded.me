import math
import uuid
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse

from .models import Sprint, SprintVirtueTally UserProfile, CustomUser


# https://blog.khophi.co/extending-django-user-model-userprofile-like-a-pro/
def create_user_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()

        sprint = Sprint(
            user_profile=user_profile,
            end_date=datetime.now() + timedelta(user_profile.sprint_length_days),
        )
        sprint.save()

post_save.connect(create_user_profile, sender=CustomUser)


def custom_user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        celery_tasks.send_verification_email.delay(instance.pk)


# TODO: move to signal
post_save.connect(custom_user_post_save, sender=CustomUser)


# TODO: move to model save method? best practices?
def create_sprint_virtue_tally(sender, **kwargs):
    virtue = kwargs["instance"]
    if kwargs["created"]:
        user_profile = virtue.user_profile
        sprint = Sprint.objects.get(user_profile_id=user_profile.id, is_active=True)
        sprint_virtue_tally = SprintVirtueTally(sprint=sprint, virtue=virtue)
        sprint_virtue_tally.save()

post_save.connect(create_sprint_virtue_tally, sender=Virtue)