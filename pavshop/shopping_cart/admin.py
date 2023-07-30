from django.contrib import admin

from .models import *
from products.models import Product


class Billing_addressAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'address', 'country', 'city', 'phone')



class Shipping_addressAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'address', 'country', 'city', 'phone')



# class BasketItemAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product', 'quantity')



# class BasketAdmin(admin.ModelAdmin):
#     list_display = ('user', 'get_items')


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user', 'basket', 'shipping_address', 'status')

# class CouponAdmin(admin.ModelAdmin):
#     list_display = ('name', 'code', 'discount', 'is_percent', 'is_active')



class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'complete', 'transaction_id')



class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity')



class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')



# Register your models here.
admin.site.register(Billing_address, Billing_addressAdmin)
admin.site.register(Shipping_address, Shipping_addressAdmin)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Customer, CustomerAdmin)



# admin.site.register(BasketItem, BasketItemAdmin)
# admin.site.register(Basket, BasketAdmin)
# admin.site.register(Order, OrderAdmin)
# admin.site.register(Coupon, CouponAdmin)
# admin.site.register(Order, OrderAdmin)
