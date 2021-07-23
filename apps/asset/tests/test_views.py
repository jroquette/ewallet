"""
Test Views of Asset
"""
from django.test import TestCase, Client
from django.urls import reverse

from apps.asset.models import Asset
from apps.account.models import Account
from apps.category.models import Category


class TestViews(TestCase):
    """
    Test Views Asset
    """
    def setUp(self) -> None:
        """
        Set up configuration to tests
        """
        Account.objects.create_user(username='teste', email='teste@teste.com', password='teste123', is_superuser=True)
        self.client = Client()
        self.client.login(username='teste', password='teste123')
        self.list_url = reverse('asset-list')
        self.test_category = Category.objects.create(name='test_category', abbreviation='category')
        self.test_asset = Asset.objects.create(name='test_asset', abbreviation='asset',
                                               category_id=self.test_category)
        self.detail_url = reverse('asset-detail', args=[self.test_asset.asset_id])

    def test_asset_list_GET(self):
        """
        Teste GET to list asset
        """
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_asset_detail_GET(self):
        """
        Teste GET detail to list asset
        """
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)

    def test_asset_detail_POST_add_new_category(self):
        """
        Test POST a new asset
        """
        response = self.client.post(self.list_url, dict(name='new_asset', abbreviation='new',
                                                        category_id=f"{self.test_category.category_id}"))
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data['name'], 'new_asset')

    def test_asset_detail_POST_no_data(self):
        """
        Test POST without data
        """
        response = self.client.post(self.list_url)
        self.assertEquals(response.status_code, 400)

    def test_asset_detail_DELETE_asset(self):
        """
        Test DELETE a asset
        """
        asset_id = self.test_asset.asset_id
        response = self.client.delete(self.detail_url, dict(id=asset_id))
        self.assertEquals(response.status_code, 204)
        response_get = self.client.get(self.detail_url)
        self.assertEquals(response_get.status_code, 404)
        self.assertEquals(response_get.status_text, 'Not Found')

