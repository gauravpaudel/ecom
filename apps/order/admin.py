from django.contrib import admin

from apps.order.models import Order, OrderItem

admin.site.register(Order)

@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity','total_price','date')
    list_filter = ('order','product')