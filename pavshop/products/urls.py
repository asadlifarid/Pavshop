from django.urls import path

from products.views import product_list_page, product_detail_page, ProductListView, ProductDetailView, export_view

urlpatterns = [
    # path('index/', views.index_page, name='index_page'),
    # path('product_detail/<int:id>/', product_detail_page, name='product_detail_page'),
    path('product_detail/<str:slug>/', ProductDetailView.as_view(), name='product_detail_page'),
    # path('product_list/', product_list_page, name='product_list_page'),
    path('product_list/', ProductListView.as_view(), name='product_list_page'),
    path('export/', export_view, name='export_view'),
    
]