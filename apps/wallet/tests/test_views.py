"""
Test Views of Asset
"""
from django.test import TestCase, Client
from django.urls import reverse

from apps.wallet.models import Wallet
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
        self.list_url = reverse('wallet-list')
        self.test_category = Category.objects.create(name='test_category', abbreviation='category')
        self.test_wallet = Wallet.objects.create(name='test_wallet', describe='wallet',
                                                 category_id=self.test_category)
        self.detail_url = reverse('wallet-detail', args=[self.test_wallet.wallet_id])

    def test_wallet_list_GET(self):
        """
        Teste GET to list wallet
        """
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_wallet_detail_GET(self):
        """
        Teste GET detail to list wallet
        """
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)

    def test_wallet_detail_POST_add_new_category(self):
        """
        Test POST a new wallet
        """
        response = self.client.post(self.list_url, dict(name='new_wallet', describe='new',
                                                        category_id=f"{self.test_category.category_id}"))
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data['name'], 'new_wallet')

    def test_wallet_detail_POST_no_data(self):
        """
        Test POST without data
        """
        response = self.client.post(self.list_url)
        self.assertEquals(response.status_code, 400)

    def test_wallet_detail_DELETE_wallet(self):
        """
        Test DELETE a wallet
        """
        wallet_id = self.test_wallet.wallet_id
        response = self.client.delete(self.detail_url, dict(id=wallet_id))
        self.assertEquals(response.status_code, 204)
        response_get = self.client.get(self.detail_url)
        self.assertEquals(response_get.status_code, 404)
        self.assertEquals(response_get.status_text, 'Not Found')
