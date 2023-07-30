from products.models import Category, Brand, Tag, Product, Discount, Property, PropertyValue, ProductImages
from django.http import JsonResponse
from products.api.serializers import (
    CategorySerializer, 
    BrandSerializer, 
    ProductSerializer, 
    TagSerializer, 
    PropertySerializer, 
    PropertyValueSerializer, 
    ProductImagesSerializer,
    ProductCreateSerializer,
    TagCreateSerializer,
    ProductImagesCreateSerializer,
    PropertyValueCreateSerializer
    )

from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView





def categories(request):
    category_list = Category.objects.all()
    # category_dict_list = []
    # for cat in category_list:
    #     category_dict_list.append({
    #         'id' : cat.id,
    #         'name' : cat.name,
    #         'slug' : cat.slug
    #     })
    serializer = CategorySerializer(category_list, many = True)
    return JsonResponse(data=serializer.data, safe=False)




def brands(request):
    brand_list = Brand.objects.all()
    # brand_dict_list = []
    # for brand in brand_list:
    #     brand_dict_list.append({
    #         'id' : brand.id,
    #         'name' : brand.name,
    #         'slug' : brand.slug
    #     })
    serializer = BrandSerializer(brand_list, many=True)
    return JsonResponse(data=serializer.data, safe=False)



@api_view(http_method_names=['GET', 'POST'])
def tags(request):
    if request.method == 'POST':
        serializer = TagCreateSerializer(data=request.data)   # form'dan gelen datani gotursun
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)  # post ise qaytarir bize
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
    tag_list = Tag.objects.all()
    # tag_dict_list = []
    # for tag in tag_list:
    #     tag_dict_list.append({
    #         'id' : tag.id,
    #         'name' : tag.name,
    #         'slug' : tag.slug,
    #         # 'products' : tag.products

    #     })
    serializer = TagSerializer(tag_list, many=True)
    return JsonResponse(data=serializer.data, safe=False)




def discounts(request):
    discount_list = Discount.objects.all()
    discount_dict_list = []
    for discount in discount_list:
        discount_dict_list.append({
            'id' : discount.id,
            'name' : discount.name,
            'value' : discount.value,
            'is_active' : discount.is_active,
            'is_percent' : discount.is_percent
        })
    return JsonResponse(data=discount_dict_list, safe=False)





# GET vs POST generic API
class ProductCreateAPIView(ListCreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()






@api_view(http_method_names=['GET', 'POST'])
def products(request):
    if request.method == 'POST':
        serializer = ProductCreateSerializer(data=request.data)   # form'dan gelen datani gotursun
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status=201)  # post ise qaytarir bize
        return JsonResponse(data=serializer.errors, safe=False, status = 400)

    product_list = Product.objects.all()
    serializer = ProductSerializer(product_list, context={'request': request}, many=True)   # ise dusen method GET-dir burda, listleyir sadece
    return JsonResponse(data=serializer.data, safe=False)




@api_view(http_method_names=['PUT', 'PATCH'])
def product_read_update(request, pk):
    if request.method == 'PUT':
        product = Product.objects.get(pk = pk)
        serializer = ProductCreateSerializer(data=request.data, instance = product, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status=201)  # post ise qaytarir bize
        return JsonResponse(data=serializer.errors, safe=False, status = 400)

    if request.method == 'PATCH':
        product = Product.objects.get(pk = pk)
        serializer = ProductCreateSerializer(data=request.data, instance = product, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status=201)  # post ise qaytarir bize
        return JsonResponse(data=serializer.errors, safe=False, status = 400)










@api_view(http_method_names=['GET', 'POST'])
def productimages(request):
    if request.method == 'POST':
        serializer = ProductImagesCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)

    productimages_list = ProductImages.objects.all()
    serializer = ProductImagesSerializer(productimages_list, context={'request': request}, many=True)
    return JsonResponse(data=serializer.data, safe=False)




def properties(request):
    property_list = Property.objects.all()
    serializer = PropertySerializer(property_list, many=True)
    return JsonResponse(data=serializer.data, safe=False)



@api_view(http_method_names=['GET', 'POST'])
def propertyvalues(request):
    if request.method == 'POST':
        serializer = PropertyValueCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)

    propertyvalue_list = PropertyValue.objects.all()
    serializer = PropertyValueSerializer(propertyvalue_list, many=True)
    return JsonResponse(data=serializer.data, safe=False)














# @api_view(http_method_names=['GET', 'POST'])
# def products(request):
#     if request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)   # form'dan gelen datani gotursun
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data=serializer.data, safe=False)  # post ise qaytarir bize
#         return JsonResponse(data=serializer.errors, safe=False)

#     product_list = Product.objects.all()
#     # product_dict_list = []
#     # for product in product_list:
#     #     product_dict_list.append({
#     #         'id' : product.id,
#     #         'title' : product.title,
#     #         'small_description' : product.small_description, 
#     #         'large_description' : product.large_description,
#     #         # 'image' : product.image,
#     #         'quantity' : product.quantity,
#     #         'in_stock' : product.in_stock,
#     #         'money' : product.money,
#     #         'slug' : product.slug,
#     #         # 'category' : product.category,
#     #         # 'brand' : product.brand,
#     #         # 'property_values' : product.property_values,
#     #         # 'discount' : product.discount
#     #     })
#     serializer = ProductSerializer(product_list, context={'request': request}, many=True)   # ise dusen method GET-dir burda, listleyir sadece
#     return JsonResponse(data=serializer.data, safe=False)

