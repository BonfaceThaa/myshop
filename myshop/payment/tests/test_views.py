import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_payment_done_success(client):
    response = client.get(reverse('payment:payment_done'))
    assert response.status_code == 200
    assert "Your payment was successful" in response.content.decode()


@pytest.mark.django_db
def test_payment_canceled_success(client):
    response = client.get(reverse('payment:payment_canceled'))
    assert response.status_code == 200
    assert "Your payment has not been processed" in response.content.decode()
