"""
Test Urls Wallet
"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from apps.wallet.views import WalletViewSet


class TestUrls(SimpleTestCase):
    """
    Test urls of wallet
    """
    def test_list_wallet_url_resolves(self):
        """
        Test list wallet
        """
        url = reverse('wallet-list')
        self.assertEquals(resolve(url).func.cls, WalletViewSet)

    def test_detail_wallet_url_resolves(self):
        """
        Test detail wallet
        """
        url = reverse('wallet-detail', args=[1])
        self.assertEquals(resolve(url).func.cls, WalletViewSet)
