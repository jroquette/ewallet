"""Urls of Account"""

from rest_framework import routers
from django.urls import path

from apps.account.views import RegistrationView, AccountViewSet


router = routers.DefaultRouter()
router.register(r'', AccountViewSet, basename='account')

urlpatterns = [
    path(r'register/', RegistrationView.as_view(), name='register')
]

account_urls = urlpatterns + router.urls
