import pytest
from rest_framework.test import APIClient
from product.models import Product

@pytest.mark.django_db
def test_create_product():
    client = APIClient()
    response = client.post(
        "/api/products/",
        {"name": "Laptop", "price": "1200.00", "active": True},
        format="json"
    )
    assert response.status_code == 201
    assert Product.objects.count() == 1
    assert Product.objects.first().name == "Laptop"
