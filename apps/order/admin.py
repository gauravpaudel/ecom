from django.contrib import admin
from apps.order.models import Order, OrderItem


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_filter = ('created_at', 'paid')


@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
    list_display = [
        'order', 'product', 'price', 'quantity',
        'total_price', 'date', 'status']
    list_filter = ['product__category']
    search_fields = ['order__first_name', 'order__last_name',
                     'product__title', 'product__category__title']
    list_editable = ['status']
