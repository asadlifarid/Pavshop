from django.contrib import admin
# from django.contrib.admin.views.main import ChangeList
from .models import *


from modeltranslation.admin import TranslationAdmin


# class ColorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'code', 'slug')



# Register your models here.

# admin.site.register(Color, ColorAdmin)
# admin.site.register(Brand)
# admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(ProductImages)
# admin.site.register(Discount, DiscountAdmin)
# admin.site.register(Tag, TagAdmin)
# admin.site.register(Review, ReviewAdmin)
# admin.site.register(Rating, RatingAdmin)
# admin.site.register(Variant, VariantAdmin)
admin.site.register(Property)
# admin.site.register(PropertyValue)
# admin.site.register(PropertyValue, PropertyValueAdmin)




@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_editable = ['name', 'slug']



@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'slug']
    list_editable = ['name', 'slug']






# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'small_description', 'large_description', 'image', 'in_stock', 'quantity', 'money', 'brand', 'category')
    

# tabular inline altda gormek istediyimizdir
# hansi modelin icinde gormek isteyirikse, onu da hemin modelin inlines = '' icine yaziriiq
class ProductInlineAdmin(admin.TabularInline):
    model = Review

class ProductImagesInlineAdmin(admin.TabularInline):
    model = ProductImages


# decorator istifade edib modeli icine gonderirik
@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = (ProductInlineAdmin, ProductImagesInlineAdmin, )
    list_display = ['id', 'title', 'image', 'in_stock', 'quantity', 'money', 'brand', 'category', 'get_tags', 'image_tag', 'slug', 'get_discount']
    list_display_links = ['title']
    list_editable = ['category', 'money', 'quantity', 'brand', 'slug']
    list_filter = ['category', 'brand']
    



    # fieldsets = (
    #     ('Main Fields', {
    #         "fields": ['id', 'title', 'description'],
    #     }),
    #     ('Other Fields', {
    #         'fields' : ['category', 'author']
    #     }),
    # )
    
    




@admin.register(PropertyValue)
class PropertyValueAdmin(admin.ModelAdmin):
    list_display = ['name', 'property']



class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'is_percent', 'is_active')



class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('image', 'product', 'image_tag')


class TagAdmin(TranslationAdmin):
    list_display = ('name', 'slug')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('rate', )

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review', 'rating', 'is_active', 'product', 'author')




admin.site.register(Discount, DiscountAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Rating, RatingAdmin)
