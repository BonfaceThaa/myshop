import pytest

from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.images import ImageFile

from shop.models import Category, Product, ProductImage


@pytest.mark.django_db
def test_create_product_success(product):
    assert Product.objects.count() == 1
    assert str(product) == product.name


@pytest.mark.django_db
def test_product_get_absolute_url(product, client):
    response = client.get(reverse('shop:product_detail', args=(product.id, product.slug)))
    assert response.status_code == 200
    assert product.name.encode() in response.content


@pytest.mark.django_db
def test_create_category_success(category):
    assert Category.objects.count() == 1


@pytest.mark.django_db
def test_category_get_absolute_url(product, client):
    response = client.get(reverse('shop:product_list_by_category', args=[product.category.slug]))
    assert response.status_code == 200
    assert product.name in response.content.decode()


# @pytest.mark.django_db
# class TestProductImage:
#
#     def test_create_product_image_success(self, test_product):
#         with open("shop/fixtures/images.jpeg", "rb") as f:
#             image = ProductImage.objects.create(
#                 product=test_product,
#                 image=ImageFile(f, name="test.jpg"),
#             )
#             # TODO : confirm the empty binary returned by f
#             # expected_content = f.read()
#             # assert image.image.read() == expected_content
#         assert ProductImage.objects.count() == 1
#         assert image.image_type == 'PRI'
#         image.image.delete(save=False)
