import weasyprint

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import OrderItem, Order, OrderComplaint
from .forms import OrderCreateForm, OrderComplaintForm
from cart.cart import Cart
from accounts.models import Profile

from .tasks import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            if request.user.is_authenticated:
                order.customer = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            order_created.delay(order.id)
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
    else:
        if request.user.is_authenticated:
            form = OrderCreateForm(initial={
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "email": request.user.email,
                "address": request.user.profile.address,
                "postal_code": request.user.profile.postal_code,
                "city": request.user.profile.city
            })
        else:
            form = OrderCreateForm()
    return render(request,
                  'orders/order/order_create.html',
                  {'cart': cart, 'form': form})


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(
        settings.STATICFILES_DIRS[0] + 'css/pdf.css'
    )])
    return response


def order_complaint(request):
    if request.method == 'POST':
        form = OrderComplaintForm(request.POST)
        if form.is_valid():
            complaint = OrderComplaint()
            complaint.order_id = form.cleaned_data['order_id']
            complaint.email = form.cleaned_data['email']
            complaint.message = form.cleaned_data['message']
            complaint.save()
            return redirect('profile')
    else:
        form = OrderComplaintForm()
    return render(request, 'orders/order/order_complaint.html', {'form': form})
