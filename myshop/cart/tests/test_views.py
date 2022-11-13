import pytest

from django.urls import reverse
from django.conf import settings

from cart.forms import CartAddProductForm
from cart.cart import Cart


@pytest.mark.django_db
def test_cart_add_form_displays(client, product):
    client.post("/cart/add/{}".format(product.id), data={'quantity': 5, 'override': False})
    response = client.get(reverse('cart:cart_detail'))
    assert response.status_code == 200
    assert 'action="/cart/add/{}"'.format(product.id) in response.content.decode()
