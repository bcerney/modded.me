from django.contrib.auth.models import AbstractUser
from django.db import models


# https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
class CustomUser(AbstractUser):
    pass


# TODO: solve UserProfile creation through signal on CustomUser creation
# https://blog.khophi.co/extending-django-user-model-userprofile-like-a-pro/
# class UserProfile(models.Model):
#     user = models.OneToOneField(
#         CustomUser,
#         on_delete=models.CASCADE,
#     )
