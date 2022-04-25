import pytest
from django.urls import reverse

from orders.forms import OrderCreateForm, OrderComplaintForm
from orders.models import Order, OrderComplaint
from .factories import OrderFactory


@pytest.mark.django_db
def test_order_create_displays_form(client):
    response = client.get(reverse('orders:order_create'))
    assert response.status_code == 200
    assert isinstance(response.context['form'], OrderCreateForm)


@pytest.mark.django_db
def test_order_create_post_success(test_order, client):
    response = client.post("/orders/create/", data=test_order)
    assert response.status_code == 302
    assert response['location'] == '/paymentprocess/'


@pytest.mark.django_db
def test_order_complaint_displays_form(client):
    response = client.get(reverse('orders:order_complaint'))
    assert response.status_code == 200
    assert isinstance(response.context['form'], OrderComplaintForm)


@pytest.mark.django_db
def test_order_complaint_post_success(client, test_order_complaint):
    order = OrderFactory()
    test_order_complaint['order_id'] = order.order_id
    response = client.post('/orders/order/complaint', data=test_order_complaint)
    assert response.status_code == 302
    assert OrderComplaint.objects.count() == 1
