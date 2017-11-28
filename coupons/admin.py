from django.contrib import admin
from .models import Coupon


class CouponAdmin(admin.ModelAdmin):
    list_display1 = ['code', 'valid_form', 'valid_to', 'discount', 'active']
    list_filter1 = ['active', 'valid_form', 'valid_to']
    search_fields1 = ['code']
admin.site.register(Coupon, CouponAdmin)
# Register your models here.
