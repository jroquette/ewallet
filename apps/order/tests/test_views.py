"""
Test Views of Order
"""
from django.test import TestCase, Client
from django.urls import reverse

from apps.order.models import Order
from apps.category.models import Category
from apps.asset.models import Asset
from apps.account.models import Account


class TestViews(TestCase):
    """
    Test Views Order
    """
    def setUp(self) -> None:
        """
        Set up configuration to tests
        """
        Account.objects.create_user(username='teste', email='teste@teste.com', password='teste123', is_superuser=True)
        self.client = Client()
        self.client.login(username='teste', password='teste123')
        self.list_url = reverse('order-list')
        self.test_category = Category.objects.create(name='test_category', abbreviation='category')
        self.test_asset = Asset.objects.create(name='test_asset', abbreviation='asset',
                                               category_id=self.test_category, price=10)
        self.test_order = Order.objects.create(asset_id=self.test_asset, quantity=2, type=0)
        self.detail_url = reverse('order-detail', args=[self.test_order.order_id])

    def test_order_list_GET(self):
        """
        Teste GET to list order
        """
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_order_detail_GET(self):
        """
        Teste GET detail to list order
        """
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)

    def test_order_detail_POST_add_new_order(self):
        """
        Test POST a new order
        """
        quantity = 5
        response = self.client.post(self.list_url, dict(asset_id=self.test_asset.asset_id, quantity=quantity, type=0))
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data['value'], (self.test_asset.price*quantity))

    def test_order_detail_POST_no_data(self):
        """
        Test POST without data
        """
        response = self.client.post(self.list_url)
        self.assertEquals(response.status_code, 400)

    def test_order_detail_DELETE_order(self):
        """
        Test DELETE a order
        """
        order_id = self.test_order.order_id
        response = self.client.delete(self.detail_url, dict(id=order_id))
        self.assertEquals(response.status_code, 204)
        response_get = self.client.get(self.detail_url)
        self.assertEquals(response_get.status_code, 404)
        self.assertEquals(response_get.status_text, 'Not Found')

