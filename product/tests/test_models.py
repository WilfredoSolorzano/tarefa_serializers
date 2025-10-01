import pytest
from product.models import Product

@pytest.mark.django_db
def test_product_str():
    product = Product.objects.create(name="Mouse", price="50.00", active=True)
    assert str(product) == "Mouse"
