from products.models import Category, Tag, Brand, PropertyValue, Product, Review
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from products.apis.serializers import (
    CategorySerializer, 
    TagSerializer, 
    BrandSerializer, 
    PropertyValueSerializer, 
    ProductSerializer, 
    ReviewSerializer,
    ProductCreateSerializer,
    ReviewCreateSerializer,
    # ProductSetPaginationSerializer
    )


# rest framework -> function-based
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.pagination import PageNumberPagination


# Pagination
from rest_framework.viewsets import ModelViewSet
from products.paginations import CustomPagination


# Search Filter in drf
from rest_framework.filters import SearchFilter


# # GET 
# def categories(request):
#     category_list = Category.objects.all()
#     # category_dict_list = []
#     # for cat in category_list:
#     #     category_dict_list.append({
#     #         'cat_id' : cat.id,
#     #         'name' : cat.name,
#     #         'slug' : cat.slug
#     #     })
#     serializer = CategorySerializer(category_list, many = True)
#     return JsonResponse(data=serializer.data, safe=False)




# POST
class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializer


# # GET
# class CategoryCreateAPIView(ListAPIView):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()


# GET ve POST -> 2-sini birlesdiren bir API View var
class CategoryCreateAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()



# DELETE ve UPDATE(PUT VE PATCH) -> 2-sini birlesdiren bir API View var
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()




# GET ve POST @api_views ile
@api_view(http_method_names=['GET', 'POST'])
def categories(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
    category_list = Category.objects.all()
    serializer = CategorySerializer(category_list, many = True)
    return JsonResponse(data=serializer.data, safe=False)





# GET 
def tags(request):
    tag_list = Tag.objects.all()
    # tag_dict_list = []
    # for tag in tag_list:
    #     tag_dict_list.append({
    #         'tag_id' : tag.id,
    #         'name' : tag.name,
    #         'slug' : tag.slug

    #     })
    serializer = TagSerializer(tag_list, many = True)
    return JsonResponse(data=serializer.data, safe=False)





# GET ve POST -> 2-sini birlesdiren bir API View var
class BrandCreateAPIView(ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()




# GET 
def brands(request):
    brand_list = Brand.objects.all()
    # brand_dict_list = []
    # for brand in brand_list:
    #     brand_dict_list.append({
    #         'brand_id' : brand.id,
    #         'name' : brand.name,
    #         'slug' : brand.slug
    #     })
    serializer = BrandSerializer(brand_list, many = True)
    return JsonResponse(data=serializer.data, safe=False)


# GET 
def propertyvalues(request):
    propertyvalue_list = PropertyValue.objects.all()
    # propertyvalue_dict_list = []
    # for propertyvalue in propertyvalue_list:
    #     propertyvalue_dict_list.append({
    #         'propertyvalue_id' : propertyvalue.id,
    #         'name' : propertyvalue.name
    #     })
    serializer = PropertyValueSerializer(propertyvalue_list, many = True)
    return JsonResponse(data=serializer.data, safe=False)



# # GET
# def products(request):
#     product_list = Product.objects.all()
#     serializer = ProductSerializer(product_list, many = True)
#     return JsonResponse(data=serializer.data, safe=False)



# POST 
class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer
    


# GET
# class ProductCreateAPIView(ListAPIView):
#     serializer_class = ProductCreateSerializer
#     queryset = Product.objects.all()



# GET ve POST -> 2-sini birlesdiren bir API View var
class ProductCreateAPIView(ListCreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()
    # pagination_class = ProductSetPaginationSerializer
    # paginator = 6
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = ['title']
    


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return self.serializer_class


    


    
    


# DELETE ve UPDATE(PUT VE PATCH) -> 2-sini birlesdiren bir API View var
class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()






# GET ve POST @api_views ile
@api_view(http_method_names=['GET', 'POST'])
def products(request):
    if request.method == 'POST':
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
    product_list = Product.objects.all()
    serializer = ProductSerializer(product_list, context = {'request' : request}, many = True)
    return JsonResponse(data=serializer.data, safe=False)



# PUT ve PATCH @api_views ile
@api_view(http_method_names=['PUT', 'PATCH'])
def product_read_update(request, pk):
    if request.method == 'PUT':
        product = Product.objects.get(pk = pk)
        serializer = ProductCreateSerializer(data=request.data, instance=product, context={'request' : request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
    if request.method == 'PATCH':
        product = Product.objects.get(pk = pk)
        serializer = ProductCreateSerializer(data=request.data, instance=product, partial = True, context={'request' : request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
   





# GET
def reviews(request):
    review_list = Review.objects.all()
    serializer = ReviewSerializer(review_list, many = True)
    return JsonResponse(data=serializer.data, safe=False)




# POST 
class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewCreateSerializer


# # GET
# class ReviewCreateAPIView(ListAPIView):
#     serializer_class = ReviewCreateSerializer
#     queryset = Review.objects.all()



# GET ve POST -> 2-sini birlesdiren bir API View var
class ReviewCreateAPIView(ListCreateAPIView):
    serializer_class = ReviewCreateSerializer
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)





# GET ve POST @api_views ile
@api_view(http_method_names=['GET', 'POST'])
def reviews(request):
    if request.method == 'POST':
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201, context={'request' : request})
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
    review_list = Review.objects.all()
    serializer = ReviewSerializer(review_list, context={'request' : request}, many = True)
    return JsonResponse(data=serializer.data, safe=False)










# # GET  serializer ehtiyac var, foreignkeyler var cunki
# def reviews(request):
#     review_list = Review.objects.all()
#     review_dict_list = []
#     for review in review_list:
#         review_dict_list.append({
#             'review_id' : review.id,
#             'product' : review.product,
#             'author' : review.author,
#             'review' : review.review,
#             'is_active' : review.is_active
#         })
#     return JsonResponse(data=review_dict_list, safe=False)
