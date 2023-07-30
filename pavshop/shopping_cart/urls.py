from django.urls import path

from shopping_cart.views import checkout_page, shopping_cart_page, CheckoutView, updateItem, processOrder


urlpatterns = [
    path('checkout/', checkout_page, name='checkout_page'),
    path('checkout/', CheckoutView.as_view(), name='checkout_page'),

    path('shop-cart/', shopping_cart_page, name='shopping_cart_page'),
    # path('shop-cart/', CartView.as_view(), name='shopping_cart_page'),


    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),

    # path('add_to_cart/', add_to_cart, name='add'),

]