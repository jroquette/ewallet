"""
Test Urls Asset
"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from apps.asset.views import AssetViewSet


class TestUrls(SimpleTestCase):
    """
    Test urls of asset
    """
    def test_list_asset_url_resolves(self):
        """
        Test list asset
        """
        url = reverse('asset-list')
        self.assertEquals(resolve(url).func.cls, AssetViewSet)

    def test_detail_asset_url_resolves(self):
        """
        Test list  asset
        """
        url = reverse('asset-detail', args=[1])
        self.assertEquals(resolve(url).func.cls, AssetViewSet)
