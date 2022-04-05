import pytest

from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.images import ImageFile

from shop.models import Category, Product, ProductImage


@pytest.mark.django_db
class TestProductModel:

    def test_create_product_success(self, test_category, client):
        product = Product.objects.create(
            category=test_category,
            name='T&G Portable Wireless Bluetooth Speakers',
            slug='t&g-portable-wireless-bluetooth-speakers',
            price=699.00
        )
        assert Product.objects.count() == 1
        assert str(product) == 'T&G Portable Wireless Bluetooth Speakers'

    def test_product_get_absolute_url(self, test_category, client):
        product = Product.objects.create(
            category=test_category,
            name='Portable Wireless Bluetooth Speakers',
            slug='portable-wireless-bluetooth-speakers',
            price=699.00
        )
        response = client.get(reverse('shop:product_detail', args=(product.id, product.slug)))
        assert response.status_code == 200
        assert b'Portable Wireless Bluetooth Speakers' in response.content


@pytest.mark.django_db
class TestCategoryModel:

    def test_create_category_success(self, category_data):
        category = Category.objects.create(**category_data)
        assert Category.objects.count() == 1
        assert category.name == 'Electronics'

    def test_category_get_absolute_url(self, product_data, client):
        product = Product.objects.create(**product_data)
        print("PRODUCT SLUG: ", product.category.slug)
        response = client.get(reverse('shop:product_list_by_category', args=[product.category.slug]))
        assert response.status_code == 200
        assert b'electronics' in response.content


@pytest.mark.django_db
class TestProductImage:

    def test_create_product_image_success(self, test_product):
        with open("shop/fixtures/images.jpeg", "rb") as f:
            image = ProductImage.objects.create(
                product=test_product,
                image=ImageFile(f, name="test.jpg"),
            )
            # TODO : confirm the empty binary returned by f
            # expected_content = f.read()
            # assert image.image.read() == expected_content
        assert ProductImage.objects.count() == 1
        assert image.image_type == 'PRI'
        image.image.delete(save=False)
