import pytest

from django.urls import reverse

from orders.models import Order, OrderItem, OrderComplaint
from .factories import OrderFactory, OrderItemFactory, OrderComplaintFactory


@pytest.mark.django_db
class TestOrderModel:

    def test_create_order_success(self):
        order = OrderFactory()
        assert Order.objects.count() == 1
        assert str(order) == f'Order {order.id}'

    def test_order_get_absolute_url(self, admin_user, client):
        order = OrderFactory(customer=admin_user)
        client.force_login(admin_user)
        response = client.get(reverse("accounts:account_order_details", args=[order.order_id]))
        assert response.status_code == 200

    def test_order_get_total_cost(self):
        order_item = OrderItemFactory()
        assert order_item.price * order_item.quantity == order_item.order.get_total_cost()


@pytest.mark.django_db
def test_order_item_create_success():
    order_item = OrderItemFactory()
    assert OrderItem.objects.count() == 1
    assert str(order_item.id) == str(order_item)


@pytest.mark.django_db
def test_order_complaint_create_success():
    order_complaint = OrderComplaintFactory()
    assert OrderComplaint.objects.count() == 1
    assert str(order_complaint) == str(order_complaint.order_id)
