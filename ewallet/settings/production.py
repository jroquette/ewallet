"""
Django settings for ewallet project development environment.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'django_redis',
]

CACHES = {
    'default': {
        "BACKEND": 'django_redis.cache.RedisCache',
        "LOCATION": f"redis://127.0.0.1:6379/1",
    }
}

# See this later
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.mailgun.org'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = True
