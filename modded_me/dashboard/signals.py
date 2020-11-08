import math
import uuid
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from manna.models import Journal, MannaProfile

from .models import CustomUser, Sprint, SprintVirtueTally, UserProfile, Virtue
from .tasks import send_verification_email


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        # setup MannaProfile
        meditate_journal = Journal(title="Meditation Journal")
        manna_profile = MannaProfile(journals=[meditate_journal])
        manna_profile.save()
        #setup UserProfile
        user_profile = UserProfile(user=user, manna_profile=manna_profile)
        user_profile.save()

        sprint = Sprint(
            user_profile=user_profile,
            end_date=datetime.now() + timedelta(user_profile.sprint_length_days),
        )
        sprint.save()


@receiver(post_save, sender=CustomUser)
def custom_user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        send_verification_email.delay(instance.pk)


# TODO: move to model save method? best practices?
@receiver(post_save, sender=Virtue)
def create_sprint_virtue_tally(sender, **kwargs):
    virtue = kwargs["instance"]
    if kwargs["created"]:
        user_profile = virtue.user_profile
        sprint = Sprint.objects.get(user_profile_id=user_profile.id, is_active=True)
        sprint_virtue_tally = SprintVirtueTally(sprint=sprint, virtue=virtue)
        sprint_virtue_tally.save()
