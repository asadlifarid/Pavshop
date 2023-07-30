from shopping_cart.models import Shipping_address, Billing_address, Product, Order, OrderItem, Customer
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import Response

from shopping_cart.api.serializers import (
    Shipping_addressSerializer, 
    Billing_addressSerializer, 
    Shipping_addressCreateSerializer,
    Billing_addressCreateSerializer,
    OrderSerializer,
    OrderItemSerializer,
    CustomerSerializer
    # BasketSerializer,
    # BasketItemSerializer
    # OrderSerializer,
    # OrderCreateSerializer,
    # OrderItemSerializer,
    # OrderItemCreateSerializer,
    # OrderItemUpdateSerializer
    )


# rest framework -> function-based
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView




# # GET
# def ship_address(request):
#     shipping_list = Shipping_address.objects.all()
#     serializer = Shipping_addressSerializer(shipping_list, many = True)
#     return JsonResponse(data=serializer.data, safe=False)




# POST 
class Billing_addressCreateAPIView(CreateAPIView):
    serializer_class = Billing_addressCreateSerializer


# # GET  - gerek urls.py da elave bir route yaradaq, o da hansi yuxarida ise o isleyecek, elverisli deyil get ve post ucun API ayri yazmaq
# class Billing_addressCreateAPIView(ListAPIView):
#     serializer_class = Billing_addressCreateSerializer
#     queryset = Billing_address.objects.all()



# GET ve POST -> 2-sini birlesdiren bir API View var
class Billing_addressCreateAPIView(ListCreateAPIView):
    serializer_class = Billing_addressCreateSerializer
    queryset = Billing_address.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)



# DELETE ve UPDATE(PUT VE PATCH) -> 2-sini birlesdiren bir API View var
class Billing_addressRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = Billing_addressSerializer
    queryset = Billing_address.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)







# POST 
class Shipping_addressCreateAPIView(CreateAPIView):
    serializer_class = Shipping_addressCreateSerializer


# # GET  - gerek urls.py da elave bir route yaradaq, o da hansi yuxarida ise o isleyecek, elverisli deyil get ve post ucun API ayri yazmaq
# class Shipping_addressCreateAPIView(ListAPIView):
#     serializer_class = Shipping_addressCreateSerializer
#     queryset = Shipping_address.objects.all()



# GET ve POST -> 2-sini birlesdiren bir API View var
class Shipping_addressCreateAPIView(ListCreateAPIView):
    serializer_class = Shipping_addressCreateSerializer
    queryset = Shipping_address.objects.all()



# DELETE ve UPDATE(PUT VE PATCH) -> 2-sini birlesdiren bir API View var
class Shipping_addressRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = Shipping_addressSerializer
    queryset = Shipping_address.objects.all()




# GET ve POST @api_views ile
@api_view(http_method_names=['GET', 'POST'])
def ship_address(request):
    if request.method == 'POST':
        serializer = Shipping_addressCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201, context={'request' : request})
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
    shipping_list = Shipping_address.objects.all()
    serializer = Shipping_addressSerializer(shipping_list, context={'request' : request}, many = True)
    return JsonResponse(data=serializer.data, safe=False)







# GET ve POST @api_views ile
@api_view(http_method_names=['GET', 'POST'])
def bill_address(request):
    if request.method == 'POST':
        serializer = Billing_addressCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201, context={'request' : request})
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
    billing_list = Billing_address.objects.all()
    serializer = Billing_addressSerializer(billing_list, context={'request' : request}, many = True)
    return JsonResponse(data=serializer.data, safe=False)






class OrderAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class OrderItemAPIView(ListCreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)



# class BasketAPIView(APIView):
#     serializer_class = BasketSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
    

#     def get(self, request, *args, **kwargs):
#         serializer = self.serializer_class(request.user.baskets)
#         return Response(serializer.data, status = 201)


#     def post(self, request, *args, **kwargs):
#         quantity = request.data.get('quantity')
#         product_id = request.data.get('product_id')
#         product = Product.objects.filter(id=product_id).first()
#         if product:
#             basket_item = BasketItem.objects.get_or_create(product=product, user=request.user)
#             basket_item2 = BasketItem.objects.get(product=product, user=request.user)
#             basket_item2.quantity += quantity
#             basket_item2.save()
#             basket, created = Basket.objects.get_or_create(user=request.user)
#             basket.items.add(basket_item2)
#             arr = []
#             for item in basket.items.all():
#                 serializer = BasketItemSerializer(item)
#                 arr.append(serializer.data)
#             message = {'success': True, 'message' : 'Product added to your card.'}
#             return Response(arr, status = 201, context={'request':request})
#         message = {'success' : False, 'message': 'Product not found.'}
#         return Response(message, status = 400)



# class BasketItemDeleteAPIView(APIView):
#     serializer_class = BasketItemSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)


#     def post(self, request, *args, **kwargs):
#         basket_item_id = request.data.get('basket_item_id')
#         BasketItem.objects.get(id=basket_item_id).delete()


    









# # GET ve POST -> 2-sini birlesdiren bir API View var
# class OrderCreateAPIView(ListCreateAPIView):
#     serializer_class = OrderCreateSerializer
#     queryset = Order.objects.all()



# # DELETE ve UPDATE(PUT VE PATCH) -> 2-sini birlesdiren bir API View var
# class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = OrderCreateSerializer
#     queryset = Order.objects.all()
#     # permission_classes = (IsAuthenticatedOrReadOnly,)




# # GET ve POST -> 2-sini birlesdiren bir API View var
# class OrderItemCreateAPIView(ListCreateAPIView):
#     serializer_class = OrderItemCreateSerializer
#     queryset = OrderItem.objects.all()



# # DELETE ve UPDATE(PUT VE PATCH) -> 2-sini birlesdiren bir API View var
# class OrderItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = OrderItemUpdateSerializer
#     queryset = OrderItem.objects.all()
#     # permission_classes = (IsAuthenticatedOrReadOnly,)


















# class OrderGetView(RetrieveUpdateDestroyAPIView):
#     serializer_class = OrderSerializer
#     queryset = Order.objects.all()




# class OrderItemUpdateView(RetrieveUpdateDestroyAPIView):
#     serializer_class = OrderItemUpdateSerializer
#     queryset = OrderItem.objects.all()

