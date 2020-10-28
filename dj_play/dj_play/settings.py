"""
Django settings for dj_play project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

import environ
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# django-environ
root = environ.Path(__file__) - 3  # get root of the project
env = environ.Env(DEBUG=(bool, False))  # set casting, default value
environ.Env.read_env()  # reading .env file

DEBUG = env("DEBUG")  # False if not in os.environ
# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env("SECRET_KEY")
# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    "default": env.db(),
    # read os.environ['SQLITE_URL']
    "extra": env.db("SQLITE_URL", default="sqlite:////tmp/my-tmp-sqlite.db"),
}

# Needed by docker = "0.0.0.0"
# TODO: find more secure practice than wildcard
ALLOWED_HOSTS = ["*"]
# TODO: breaking connection on test-deploy right now, investigate
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True


# Application definition

INSTALLED_APPS = [
    # default
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Django tutorial
    "quotes_app.apps.QuotesAppConfig",
    "get_lucky_draw.apps.GetLuckyDrawConfig",
    "dashboard.apps.DashboardConfig",
    # django-taggit
    # https://github.com/jazzband/django-taggit
    "taggit",
    "taggit_serializer",
    # django-bootstrap4
    "bootstrap4",
    # https://django-extensions.readthedocs.io/en/latest/installation_instructions.html
    "django_extensions",
    # DRF tutorial
    # https://www.django-rest-framework.org/tutorial/1-serialization/
    # 'rest_framework',
    # 'quotes_api.apps.QuotesApiConfig',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "dj_play.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR.joinpath("templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dj_play.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "postgres",
#         "USER": "postgres",
#         "PASSWORD": "postgres",
#         "HOST": "db",
#         "PORT": 5432,
#     }
# }

AUTH_USER_MODEL = "dashboard.CustomUser"

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# DRF
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}


# auth
# https://learndjango.com/tutorials/django-login-and-logout-tutorial
# https://learndjango.com/tutorials/django-signup-tutorial

LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/"

# django-bootstrap4
# https://django-bootstrap4.readthedocs.io/en/latest/settings.html
BOOTSTRAP4 = {
    "error_css_class": "bootstrap4-error",
    "required_css_class": "bootstrap4-required",
    "javascript_in_head": True,
    "include_jquery": True,
}
