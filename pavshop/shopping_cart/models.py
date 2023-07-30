from django.db import models
# from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# from authentication.models import User

from djmoney.models.fields import MoneyField
from djmoney.money import Money
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
from djmoney.contrib.exchange.models import convert_money

from django_countries.fields import CountryField

from base.models import AbstractModel

from django.core.validators import MinValueValidator, MaxValueValidator

from products.models import *

from django.contrib.auth import get_user_model

User = get_user_model()


DIRECT_BANK_TRANSFER = "direct bank transfer"
CASH_ON_DELIVERY = "cash on delivery"
CHEQUE_PAYMENT = "cheque payment"
PAYPAL = "paypal"


CHOICES = (
    (DIRECT_BANK_TRANSFER, "Direct Bank Transfer"),
    (CASH_ON_DELIVERY, "Cash On Delivery"),
    (CHEQUE_PAYMENT, "Cheque Payment"),
    (PAYPAL, "Paypal"),
)




# checkout page ucun: 2 form

class Shipping_address(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    address = models.TextField()
    country = CountryField(blank_label="(select country)")
    city = models.CharField(max_length=255)
    phone = PhoneNumberField()
    
    
    
    def __str__(self):
        return '{} {} {} {}'.format(self.user, self.company, self.address, self.city)


    def user_name(self):
        return self.user.get_full_name()




# Create your models here.  - BillShipInfo modeli
class Billing_address(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    address = models.TextField()
    country = CountryField(blank_label="(select country)")
    city = models.CharField(max_length=255)
    phone = PhoneNumberField()
    shipping_address = models.ForeignKey(Shipping_address, on_delete=models.CASCADE, null=True, blank=True)
    
    

    # class Meta:
    #     verbose_name = "Billing_address"
    #     verbose_name_plural = "Billing_addresses"


    def __str__(self):
        return '{} {} {} {} {}'.format(self.user, self.company, self.address, self.city, self.shipping_address)


    def user_name(self):
        return self.user.get_full_name()





# Order item
# class BasketItem(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='basket_items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='basket_items', null=True, blank=True)
#     # basket = models.ForeignKey(Basket, on_delete=models.CASCADE, null=True, blank=True, related_name='basket_items')
#     quantity = models.IntegerField(default=0, null=True, blank=True)
   
    

#     def __str__(self):
#         return '{} {} {}'.format(self.quantity, self.product, self.user)
    



# # Order
# class Basket(models.Model):
#     # related_name = "shoppingcardofUser"
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='baskets', null=True, blank=True)
#     items = models.ManyToManyField(BasketItem, related_name='basket_items')
#     # status = models.CharField(max_length=255, choices = STATUS_CHOICES, default=1, blank=True, null=True)
#     # transaction_id = models.CharField(max_length=100, null=True, blank=True)



#     # def user_name(self):
#     #     return self.request.user.get_full_name()
   
    
#     def __str__(self):

#         return f"{self.user.username}'s Shopping Card"
#         # return '{} {}'.format(self.user, self.transaction_id)


#     # def user_name(self):
#     #     return self.request.user.get_full_name()

#     def get_items(self):
#         # print(Tags.stories)
#         return '\n'.join([str(p) for p in self.items.all()])



# # class Coupon(AbstractModel):
# #     name = models.CharField(max_length=50)   # yaz endirimi
# #     code = models.IntegerField()           # 1094
# #     discount = models.IntegerField()         # 20
# #     is_percent = models.BooleanField()            
# #     is_active = models.BooleanField()


# #     def __str__(self):
# #         return '{} {} {} {} {}'.format(self.name, self.code, self.discount, self.is_percent, self.is_active)



# class Order(models.Model):
#     STATUS = (
#         (1, 'Pending'),
#         (2, 'Order Confirmed'),
#         (3, 'Out for Delivery'),
#         (4, 'Delivered'),
#     )

#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
#     basket = models.ForeignKey(Basket, on_delete=models.SET_NULL, related_name='orders', null=True)
#     shipping_address = models.ForeignKey(Shipping_address, related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)
    
#     # ordered field
#     status = models.IntegerField(choices=STATUS, default=1, null=True, blank=True)
#     # sub_total = models.IntegerField()   # endirimsiz total; endirim olanda ise onu views.py da hesablayacagiq;
    
#     # product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     # coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, related_name='orders', default=False)
   


#     def __str__(self):
#         return '{} {} {} {}'.format(self.status, self.basket, self.user, self.shipping_address)





class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.user.username
    
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True)


    def __str__(self):
        return str(self.id)

    @property
    def get_grand_total(self):
        orderitems = self.order_items.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.order_items.all()
        total = sum([item.quantity for item in orderitems])
        return total



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name='order_items')
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    # def get_total(self):
    #     total = self.quantity * self.product.money
    #     return total
    
    @property
    def get_total(self):
        total = self.quantity * self.product.apply_discount()
        return total

    