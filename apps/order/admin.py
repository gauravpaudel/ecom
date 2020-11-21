from django.contrib import admin

from apps.order.models import Order, OrderItem

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_filter = ('created_at','paid')




@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity','total_price','date')
    list_filter = ('order','product')

