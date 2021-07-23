"""
Test Urls Category
"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from apps.category.views import CategoryViewSet


class TestUrls(SimpleTestCase):
    """
    Test urls of category
    """
    def test_list_category_url_resolves(self):
        """
        Test list categories
        """
        url = reverse('category-list')
        self.assertEquals(resolve(url).func.cls, CategoryViewSet)

    def test_detail_category_url_resolves(self):
        """
        Test list category detail
        """
        url = reverse('category-detail', args=[1])
        self.assertEquals(resolve(url).func.cls, CategoryViewSet)
