import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_list_product_success(product, client):
    response = client.get(reverse('shop:product_list'))
    assert response.status_code == 200
    assert product.name in response.content.decode()
    assert product.category.name in response.content.decode()


@pytest.mark.django_db
def test_list_product_by_category_success(product, client):
    response = client.get(reverse('shop:product_list_by_category', args=[product.category.slug]))
    assert response.status_code == 200
    assert product.category.name in response.content.decode()


@pytest.mark.django_db
def test_product_detail(product, client):
    response = client.get(reverse('shop:product_detail', args=[product.id, product.slug]))
    assert response.status_code == 200
    assert product.name in response.content.decode()


def test_custom_not_found_success(client):
    response = client.get('/cato/')
    assert response.status_code == 404
    assert "404" in response.content.decode()
