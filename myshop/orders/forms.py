from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _

from .models import Order, OrderComplaint


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']


class OrderComplaintForm(forms.ModelForm):

    class Meta:
        model = OrderComplaint
        fields = ('order_id', 'email', 'message')

    def clean_order_id(self):
        order_id = self.cleaned_data['order_id']
        if Order.objects.filter(order_id=order_id).exists():
            if OrderComplaint.objects.filter(order_id=order_id).exists():
                raise forms.ValidationError('Issue with this order ID has already being raised!')
        else:
            raise forms.ValidationError("No order ID found. Please confirm the order ID!")
        return order_id

