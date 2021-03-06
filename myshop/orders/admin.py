import csv
import datetime

from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Order, OrderItem, OrderComplaint


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    file_date = datetime.datetime.now()
    file_date = file_date.strftime('-%b-%d-%Y')
    content_disposition = f'attachment; filename={opts.verbose_name}{file_date}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow(field.verbose_name for field in fields)
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d%m%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_to_csv.short_description = 'Export orders to CSV'


def order_pdf(obj):
    url = reverse('orders:admin_order_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">Invoice PDF</a>')


order_pdf.short_description = 'Invoice'


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'first_name', 'last_name', 'email', 'paid', 'created',
                    'updated', order_pdf]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInLine]
    actions = [export_to_csv]

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(OrderComplaint)
class OrderComplaintAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'email']

