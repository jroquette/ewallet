"""
Test Views of Category
"""
from django.test import TestCase, Client
from django.urls import reverse

from apps.category.models import Category
from apps.account.models import Account


class TestViews(TestCase):
    """
    Test Views Category
    """
    def setUp(self) -> None:
        """
        Set up configuration to tests
        """
        Account.objects.create_user(username='teste', email='teste@teste.com', password='teste123', is_superuser=True)
        self.client = Client()
        self.client.login(username='teste', password='teste123')
        self.list_url = reverse('category-list')
        self.test_category = Category.objects.create(name='test_category', abbreviation='category')
        self.detail_url = reverse('category-detail', args=[self.test_category.category_id])

    def test_category_list_GET(self):
        """
        Teste GET to list category
        """
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_category_detail_GET(self):
        """
        Teste GET detail to list category
        """
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)

    def test_category_detail_POST_add_new_category(self):
        """
        Test POST a new category
        """
        response = self.client.post(self.list_url, dict(name='new_category', abbreviation='new'))
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data['name'], 'new_category')

    def test_category_detail_POST_no_data(self):
        """
        Test POST without data
        """
        response = self.client.post(self.list_url)
        self.assertEquals(response.status_code, 400)

    def test_category_detail_DELETE_category(self):
        """
        Test DELETE a category
        """
        category_id = self.test_category.category_id
        response = self.client.delete(self.detail_url, dict(id=category_id))
        self.assertEquals(response.status_code, 204)
        response_get = self.client.get(self.detail_url)
        self.assertEquals(response_get.status_code, 404)
        self.assertEquals(response_get.status_text, 'Not Found')

