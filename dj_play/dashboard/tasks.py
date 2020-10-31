import logging

from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse

from dj_play.celery import app


@shared_task
def hello():
    print("Hello World")

# TODO: better understand shared vs app task
@app.task
def send_verification_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        send_mail(
            'Verify your Modded.Me account',
            'Follow this link to verify your account: '
                f"http://0.0.0.0:80{reverse('dashboard:verify', kwargs={'uuid': str(user.verification_uuid)})}",
            'from@modded.me',
            [user.email],
            fail_silently=False,
        )
    except UserModel.DoesNotExist:
        logging.warning(f"Tried to send verification email to non-existing user '{user.id}'")