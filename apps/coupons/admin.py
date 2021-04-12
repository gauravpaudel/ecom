from django.contrib import admin
from apps.coupons.models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount', 'active', 'num_available', 'num_used', ]
    list_filter = ['active']
    search_fields = ['code']
