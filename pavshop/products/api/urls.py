from django.urls import path
from products.api.views import (
    categories, 
    brands, 
    tags, 
    discounts, 
    products, 
    properties, 
    propertyvalues, 
    productimages, 
    product_read_update, 
    ProductCreateAPIView
)



urlpatterns = [
    # path('products/', products, name='products'),
    path('products/', ProductCreateAPIView.as_view(), name='products'),

    path('products/<int:pk>/', product_read_update, name='product_read_update'),
    
    path('products/categories/', categories, name='categories'),
    path('products/brands/', brands, name='brands'),
    path('products/properties/', properties, name='properties'),
    path('products/propertyvalues/', propertyvalues, name='propertyvalues'),
    path('products/productimages/', productimages, name='productimages'),
    
    path('products/tags/', tags, name='tags'),
    path('products/discounts/', discounts, name='discounts'),
    
]
