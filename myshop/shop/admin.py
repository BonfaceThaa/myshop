from django.contrib import admin
from django.utils import timezone

from .models import Category, Product, ProductImage


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    exclude = 'deleted_at',
    inlines = [ProductImageAdmin]

    def get_queryset(self, request):
        """
        Function to filter out products that have been soft deleted
        :param request:
        :return:
        """
        qs = super().get_queryset(request)
        return qs.filter(deleted_at__isnull=True)

    def delete_queryset(self, request, queryset):
        """
        Function to update the deleted_at field with current time upon soft delete
        :param request:
        :param queryset:
        :return:
        """
        for obj in queryset:
            obj.deleted_at = timezone.now()
            obj.save()
