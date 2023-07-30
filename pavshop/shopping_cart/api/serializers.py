from rest_framework import serializers
from shopping_cart.models import Shipping_address, Billing_address, Customer, Order, OrderItem 
from products.apis.serializers import ProductSerializer

# GET
class Shipping_addressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping_address
        fields = (
            'id',
            # 'user',
            'user_name',
            'company',
            'address',
            'country',
            'city',
            'phone'
        )


# POST
class Shipping_addressCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Shipping_address
        fields = (
            'id',
            'user',
            'company',
            'address',
            'country',
            'city',
            'phone'
        )


    def validate(self, attrs):
        request = self.context['request']
        attrs['user'] = request.user
        return super().validate(attrs)



# GET
class Billing_addressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing_address
        fields = (
            'id',
            # 'user',
            'user_name',
            'company',
            'address',
            'country',
            'city',
            'phone',
            'shipping_address'
        )



# POST
class Billing_addressCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Billing_address
        fields = (
            'id',
            'user',
            'company',
            'address',
            'country',
            'city',
            'phone',
            'shipping_address'
        )

    def validate(self, attrs):
        request = self.context['request']
        attrs['user'] = request.user
        return super().validate(attrs)






class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id',
            'user',
            'name',
            'email'
        )



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'customer',
            'complete',
            'transaction_id'
        )



class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'id',
            'product',
            'order',
            'quantity',
            
        )