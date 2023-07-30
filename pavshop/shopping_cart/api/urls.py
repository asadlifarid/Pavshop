from django.urls import path
from shopping_cart.api.views import (
    ship_address, 
    bill_address, 
    Billing_addressCreateAPIView,
    Shipping_addressCreateAPIView,
    Shipping_addressRetrieveUpdateDestroyAPIView,
    Billing_addressRetrieveUpdateDestroyAPIView,
    OrderAPIView,
    OrderItemAPIView
    
    
    )


urlpatterns = [
    # path('shipping/', ship_address, name='ship_address'),
    path('shipping/', Shipping_addressCreateAPIView.as_view(), name='ship_address'),
    path('shipping/<int:pk>/', Shipping_addressRetrieveUpdateDestroyAPIView.as_view(), name='ship_address'),

    # path('billing/', bill_address, name='bill_address'),
    path('billing/', Billing_addressCreateAPIView.as_view(), name='bill_address'),
    path('billing/<int:pk>/', Billing_addressRetrieveUpdateDestroyAPIView.as_view(), name='bill_address'),

    path('orders/', OrderAPIView.as_view(), name='orders'),
    path('order-items/', OrderItemAPIView.as_view(), name='order_items')
    


]
