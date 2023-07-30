from django.urls import path
from products.apis.views import (
    categories, 
    tags, 
    brands, 
    propertyvalues, 
    products, 
    reviews, 
    product_read_update, 
    ProductCreateAPIView,
    ReviewCreateAPIView,
    CategoryCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    CategoryRetrieveUpdateDestroyAPIView, 
    BrandCreateAPIView
    )



urlpatterns = [
    # path('products/', products, name='products'),
    path('products/', ProductCreateAPIView.as_view(), name='products'),
    # path('products/categories/', categories, name='categories'),
    path('products/categories/', CategoryCreateAPIView.as_view(), name='categories'),
    path('products/tags/', tags, name='tags'),
    # path('products/brands/', brands, name='brands'),
    path('products/brands/', BrandCreateAPIView.as_view(), name='brands'),

    path('products/propertyvalues/', propertyvalues, name='propertyvalues'),
    # path('products/reviews/', reviews, name='reviews'),
    path('products/reviews/', ReviewCreateAPIView.as_view(), name='reviews'),

    # path('products/<int:pk>/', product_read_update, name='product_read_update'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_read_update'),
    path('products/categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='categories'),




]
