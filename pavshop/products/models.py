from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models import Count

from base.models import AbstractModel

# from djmoney.models.fields import MoneyField
# from djmoney.money import Money
from decimal import Decimal
# from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
from djmoney.contrib.exchange.models import convert_money

from django.db.models import Avg

from django.urls import reverse, reverse_lazy

from django.utils.html import mark_safe

User = get_user_model()

# from phonenumber_field.modelfields import PhoneNumberField




# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True, max_length=255)
    

    def __str__(self):
        return '{} {}'.format(self.name, self.slug)



# class Color(models.Model):
#     name = models.CharField(max_length=255)
#     code = models.CharField(max_length=10, null=True, blank=True)
#     slug = models.SlugField(null=True, blank=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name="products")

#     # product = models.ManyToManyField(Product, default=None, related_name="products")

#     class Meta:
#         ordering = ['name',] 


#     def __str__(self):
#         return '{} {}'.format(self.name, self.slug)

# class Color(models.Model):
#     name = models.CharField(max_length=255)
#     code = models.CharField(max_length=10, null=True, blank=True)
#     slug = models.SlugField(null=True, blank=True)
#     # product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE, related_name="products")

#     # product = models.ManyToManyField(Product, default=None, related_name="products")

#     # class Meta:
#     #     ordering = ['name',] 


#     def __str__(self):
#         return '{} {}'.format(self.name, self.slug)





class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True, max_length=255)


    # @classmethod
    # def count_cat(cls):
    #     return cls.objects.count()


    def __str__(self):
        return '{} {}'.format(self.name, self.slug)





class Property(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"




class PropertyValue(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="values")
    
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Property Value"
        verbose_name_plural = "Property Values"






class Discount(AbstractModel):
    name = models.CharField(max_length=255)  # yaz endirimi
    value = models.DecimalField(max_digits=6, decimal_places=2)   # 20
    is_percent = models.BooleanField(default=True)   # %
    is_active = models.BooleanField(default=False)    # True/False
    # product = models.ManyToManyField(Product, related_name="discounts")
    

    def __str__(self):
        return '{} {} {} {}'.format(self.name, self.value, self.is_percent, self.is_active)



    


class Tag(models.Model):
    name = models.CharField(max_length=255)
    # products = models.ManyToManyField(Product)
    slug = models.SlugField(null=True, blank=True, max_length=255)


    def __str__(self):
        return '{} {}'.format(self.name, self.slug)





class Product(AbstractModel):
    QUANTITY_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),

    )
    title = models.CharField(max_length=255)
    small_description = models.TextField(null=True, blank=True)
    large_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product_images')
    in_stock = models.BooleanField(default=True)
    quantity = models.IntegerField(choices=QUANTITY_CHOICES, default=1, null=True, blank=True)

    # status = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True, max_length=255) 

    money = models.DecimalField(max_digits=5, decimal_places=2)

    # money = MoneyField( 
    #     max_digits=14, 
    #     decimal_places=2, 
    #     default_currency='USD',
    #     validators=[
    #         MinMoneyValidator(Decimal(0.00)), 
    #         MaxMoneyValidator(Decimal(9999.99)),

    #     ]
    # )

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True, related_name="products")
    # color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    property_values = models.ManyToManyField(PropertyValue)
    discount = models.ManyToManyField(Discount, related_name="products")
    tag = models.ManyToManyField(Tag)

    


    # class Meta:
    #     ordering = ['-title',] 


    def __str__(self):
        return self.title


    def get_tags(self):
        return '\n'.join([str(p) for p in self.tag.all()])
        

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.image.url))
    # image_tag.short_description = 'Image


    def get_absolute_url(self, **kwargs):
        return reverse_lazy("product_detail_page", kwargs={"slug": self.slug})


    def get_discount(self):
        # print(Tags.stories)
        return '\n'.join([str(p) for p in self.discount.all()])


    
    def apply_discount(self):
        discount_percent = sum(d.value for d in self.discount.all() if d.is_percent and d.is_active)
        discount_fixed = sum(d.value for d in self.discount.all() if d.is_percent is False and d.is_active)

        if discount_percent:
            return float(self.money - (self.money * discount_percent) / 100)
        elif discount_fixed:
            return self.money - discount_fixed
        return self.money


    def get_quantity_display(self):
        if self.quantity == 1:
            return dict(Product.QUANTITY_CHOICES)[1]
        elif self.quantity == 2:
            return dict(Product.QUANTITY_CHOICES)[2]
        elif self.quantity == 3:
            return dict(Product.QUANTITY_CHOICES)[3]
        elif self.quantity == 4:
            return dict(Product.QUANTITY_CHOICES)[4]
        elif self.quantity == 5:
            return dict(Product.QUANTITY_CHOICES)[5]

    
    def get_quantity(self):
        arr = []
        if self.quantity > 1:
            for i in range(self.quantity, 0, -1):
                arr.append(i)
        return arr
    


    def average_rating(self):
        if Review.objects.filter(product=self).aggregate(Avg('rating'))['rating__avg']:
            return '%.1f' % (Review.objects.filter(product=self).aggregate(Avg('rating'))['rating__avg'])
        return 0

    # def property_values_name(self):
    #     return self.property_values.name
        
    
                






    # def get_color(self):
    #     # print(Tags.stories)
    #     return '\n'.join([str(p) for p in self.color.all()])
    



# class Property(models.Model):
#     name = models.CharField(max_length=255)


#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Property"
#         verbose_name_plural = "Properties"




# class PropertyValue(models.Model):
#     property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="values")
    
#     name = models.CharField(max_length=255)


#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Property Value"
#         verbose_name_plural = "Property Values"


# class Variant(models.Model):
#     title = models.CharField(max_length=255, blank=True, null=True)
#     image = models.ImageField(upload_to='variants')
    
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
#     color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True, related_name="variants")
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="variants")

#     quantity = models.IntegerField(default=1)
#     money = MoneyField( 
#         max_digits=14, 
#         decimal_places=2, 
#         default_currency='USD',
#         validators=[
#             MinMoneyValidator(Decimal(0.00)), 
#             MaxMoneyValidator(Decimal(9999.99)),

#         ]
#     )
    


#     def __str__(self):
#         return self.title
    





   

# class Color(models.Model):
#     name = models.CharField(max_length=255)
#     code = models.CharField(max_length=10, null=True, blank=True)
#     slug = models.SlugField(null=True, blank=True)
#     # product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE, related_name="products")

#     # product = models.ManyToManyField(Product, default=None, related_name="products")

#     class Meta:
#         ordering = ['name',] 


#     def __str__(self):
#         return '{} {}'.format(self.name, self.slug)





# class Tag(models.Model):
#     name = models.CharField(max_length=255)
#     products = models.ManyToManyField(Product)
#     slug = models.SlugField(null=True, blank=True, max_length=255)


#     def __str__(self):
#         return '{} {} {}'.format(self.name, self.products, self.slug)




# class Discount(AbstractModel):
#     name = models.CharField(max_length=255)  # yaz endirimi
#     value = models.IntegerField()     # 20
#     is_percent = models.BooleanField(default=True)   # %
#     is_active = models.BooleanField(default=False)    # True/False
#     # product = models.ManyToManyField(Product, related_name="discounts")
    

#     def __str__(self):
#         return '{} {} {} {} {}'.format(self.name, self.value, self.is_percent, self.is_active)

    
    # def get_discount(self):
    #     # print(Tags.stories)
    #     return '\n'.join([str(p) for p in self.product.all()])


    # @property
    # def discount_percantage(self):
    #     if self.is_percent is True and self.is_active is True:
    #         result1 = (self.product.money * self.value) / 100
    #         result = self.product.money - result1
    #         print(result1)
    #         print(result)
    #         return result
    #         # return (100 * value) / product.money






# 1 mehsul, coxlu sekil ucun
class ProductImages(models.Model):
    image = models.ImageField(upload_to="products_images")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products_images")
    # variant = models.ForeignKey(Variant, on_delete=models.CASCADE, related_name="products_images")
   


    def __str__(self):
        return '{} {}'.format(self.image, self.product)


    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.image.url))

    # image_tag.short_description = 'Image'



class Rating(models.Model):
    rate = models.IntegerField()


    def __str__(self):
        return str(self.rate)
    


class Review(AbstractModel):
    # yeni, product field  "reviews" adli related_name ile Product modeline baglanir burada
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # name = models.CharField(max_length=255)
    # email = models.EmailField(blank=True)
    review = models.TextField()
    rating = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return '{} {} {} {} {}'.format(self.review, self.product, self.author, self.rating, self.is_active)

    # def __str__(self):
    #     return self.product.title  - hansi producta bagli oldugunu gormeliyik


    def author_name(self):
        return self.author.get_full_name()
    
