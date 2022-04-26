import pytest

from django.urls import reverse

from coupons.forms import CouponApplyForm
from .factories import CouponFactory


@pytest.mark.django_db
def test_coupon_displays_form(client):
    response = client.get(reverse('cart:cart_detail'))
    assert response.status_code == 200
    assert isinstance(response.context['coupon_apply_form'], CouponApplyForm)


@pytest.mark.django_db
def test_coupon_post_success(client):
    coupon = CouponFactory(active=True)
    response = client.post('/coupons/apply/', data={"code": coupon.code})
    assert response.status_code == 302
    assert response['location'] == '/cart/'
