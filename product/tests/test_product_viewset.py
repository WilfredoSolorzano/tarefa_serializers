from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from product.models import Product

class ProductViewSetTest(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(name="Notebook", price=3500, active=True)
        self.url = reverse('product-list')

    def test_list_products(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Notebook')

    def test_create_product(self):
        data = {"name": "Mouse", "price": 150, "active": True}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_retrieve_product(self):
        url_detail = reverse('product-detail', args=[self.product.id])
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Notebook')

    def test_update_product(self):
        url_detail = reverse('product-detail', args=[self.product.id])
        data = {"name": "Notebook Gamer", "price": 4500, "active": True}
        response = self.client.put(url_detail, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, "Notebook Gamer")

    def test_delete_product(self):
        url_detail = reverse('product-detail', args=[self.product.id])
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
