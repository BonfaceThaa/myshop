import pytest
from django.urls import reverse

from orders.models import Order, OrderComplaint


@pytest.mark.django_db
def test_create_order_complaint_success(test_order):
    order_complaint = OrderComplaint.objects.create(order_id=test_order.order_id, email="user@email.com", message="Requesting for a refund")
    assert OrderComplaint.objects.count() == 1
    assert str(order_complaint) == test_order.order_id


@pytest.mark.django_db
class TestOrderModel:

    def test_create_order_success(self, order_data):
        order = Order.objects.create(**order_data)
        assert Order.objects.count() == 1
        assert str(order) == f'Order {order.id}'

    def test_order_get_absolute_url(self, admin_user, order_data, client):
        order = Order.objects.create(customer=admin_user, **order_data)
        response = client.get(reverse("accounts:account_order_details", args=[order.order_id]))
        assert response.status_code == 200
