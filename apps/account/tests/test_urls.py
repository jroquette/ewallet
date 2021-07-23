"""
Test Urls Account
"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from apps.account.views import AccountViewSet, RegistrationView


class TestUrls(SimpleTestCase):
    """
    Test urls of account
    """
    def test_list_account_url_resolves(self):
        """
        Test list account
        """
        url = reverse('account-list')
        self.assertEquals(resolve(url).func.cls, AccountViewSet)

    def test_detail_account_url_resolves(self):
        """
        Test list  account
        """
        url = reverse('account-detail', args=[1])
        self.assertEquals(resolve(url).func.cls, AccountViewSet)

    def test_register_account_url_resolves(self):
        """
        Test list account
        """
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, RegistrationView)