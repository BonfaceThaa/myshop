from celery import task
from django.core.mail import send_mail

from .models import Order


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order number: {order.id}'
    message = f'Dear {order.first_name}, you have successfully placed an order. Your Order number is: {order.id}'
    mail_sent = send_mail(subject, message, 'thaabonface@gmail.com', [order.email])
    return mail_sent
