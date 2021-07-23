"""
Test Urls Order
"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from apps.order.views import OrderViewSet


class TestUrls(SimpleTestCase):
    """
    Test urls of order
    """
    def test_list_order_url_resolves(self):
        """
        Test list orders
        """
        url = reverse('order-list')
        self.assertEquals(resolve(url).func.cls, OrderViewSet)

    def test_detail_order_url_resolves(self):
        """
        Test list order detail
        """
        url = reverse('order-detail', args=[1])
        self.assertEquals(resolve(url).func.cls, OrderViewSet)
