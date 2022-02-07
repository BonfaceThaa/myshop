import string
import random

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Order


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def order_id_gen(instance):
    order_id = id_generator()
    Order = instance.__class__
    qs = Order.objects.filter(order_id=order_id).exists()
    if qs:
        return order_id_gen(instance)
    return order_id


@receiver(pre_save, sender=Order)
def save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = order_id_gen(instance)


pre_save.connect(save_create_order_id, sender=Order)