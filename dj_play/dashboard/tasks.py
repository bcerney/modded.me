import logging
from random import choice

from celery import shared_task
from dj_play.celery import app
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from quotes_app.models import Quote

from .models import Sprint, Virtue


# @shared_task
# def hello():
#     print("Hello World")


# TODO: better understand shared vs app task
@app.task
def send_verification_email(user_id):
    UserModel = settings.AUTH_USER_MODEL
    try:
        user = UserModel.objects.get(pk=user_id)
        send_mail(
            "Verify your Modded.Me account",
            "Follow this link to verify your account: "
            f"http://{settings.EMAIL_SITE_DOMAIN}{reverse('dashboard:verify', kwargs={'uuid': str(user.verification_uuid)})}",
            "from@modded.me",
            [user.email],
            fail_silently=False,
        )
    except UserModel.DoesNotExist:
        logging.warning(
            f"Tried to send verification email to non-existing user '{user.id}'"
        )

@shared_task
def send_daily_snapshot_email(user_id):
    context = {}
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        user_profile = user.userprofile
        context['user'] = user

        try:
            quote = choice(Quote.objects.filter(user=user))
        except IndexError:
            # TODO: add default quotes from some default quote user
            quote = None
        context["quote"] = quote

        virtues = Virtue.objects.filter(user_profile_id=user_profile.id).all()
        context["virtues"] = virtues

        sprint = Sprint.objects.get(user_profile_id=user_profile.id, is_active=True)
        context["sprint"] = sprint

        msg_txt = render_to_string('email/daily-snapshot.txt', context)
        # TODO: solve bootstrap in email issue
        # msg_html = render_to_string('dashboard/dashboard.html', context)

        send_mail(
            # TODO: generate date, add to email title
            "Modded.Me Daily Snapshot",
            msg_txt,
            "from@modded.me",
            [user.email],
            # html_message=msg_html,
            fail_silently=False,
        )
    except UserModel.DoesNotExist:
        logging.warning(
            f"Non-existing user '{user.id}'"
        )

