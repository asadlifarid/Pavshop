from blogs.models import Category, Tag, Story, Comment
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blogs.apis.serializers import (
    CategorySerializer, 
    TagSerializer, 
    StorySerializer, 
    CommentSerializer, 
    StoryCreateSerializer,
    CommentCreateSerializer
)

# rest framework -> function-based
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView




# # bunlarin hamisi GET methoddur, cagiririq sadece
# # GET
# def categories(request):
#     category_list = Category.objects.all()
#     # category_dict_list = []
#     # for cat in category_list:
#     #     category_dict_list.append({
#     #         'cat_id' : cat.id,
#     #         'name' : cat.title
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
    '''
       Sample
    '''
    serializer_class = CategorySerializer
    queryset = Category.objects.all()



# DELETE ve UPDATE(PUT VE PATCH) -> 2-sini birlesdiren bir API View var
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()





# GET ve POST -> 2-sini birlesdiren bir API View var
class TagCreateAPIView(ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()



# DELETE ve UPDATE(PUT VE PATCH) -> 2-sini birlesdiren bir API View var
class TagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()





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
    #         'name' : tag.name
    #     })
    serializer = TagSerializer(tag_list, many = True)
    return JsonResponse(data=serializer.data, safe=False)


# GET
# def stories(request):
#     story_list = Story.objects.all()
#     serializer = StorySerializer(story_list, many = True)
#     return JsonResponse(data=serializer.data, safe=False)




# GET
def comments(request):
    comment_list = Comment.objects.all()
    serializer = CommentSerializer(comment_list, many = True)
    return JsonResponse(data=serializer.data, safe=False)



# POST 
# class StoryCreateAPIView(CreateAPIView):
#     serializer_class = StoryCreateSerializer


# # GET  - gerek urls.py da elave bir route yaradaq, o da hansi yuxarida ise o isleyecek, elverisli deyil get ve post ucun API ayri yazmaq
# class StoryCreateAPIView(ListAPIView):
#     serializer_class = StoryCreateSerializer
#     queryset = Story.objects.all()



# GET ve POST -> 2-sini birlesdiren bir API View var
class StoryCreateAPIView(ListCreateAPIView):
    serializer_class = StoryCreateSerializer
    queryset = Story.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StorySerializer
        return self.serializer_class



# DELETE ve UPDATE(PUT VE PATCH) -> 2-sini birlesdiren bir API View var
class StoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = StoryCreateSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Story.objects.all()





#  POST 
class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentCreateSerializer


# # GET
# class CommentCreateAPIView(ListAPIView):
#     serializer_class = CommentCreateSerializer
#     queryset = Comment.objects.all()



# GET ve POST -> 2-sini birlesdiren bir API View var
class CommentCreateAPIView(ListCreateAPIView):
    serializer_class = CommentCreateSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)







# GET ve POST @api_views ile
@api_view(http_method_names=['GET', 'POST'])
def comments(request):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, context={'request' : request}, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
    comment_list = Comment.objects.all()
    serializer = CommentSerializer(comment_list, context={'request' : request}, many = True)
    return JsonResponse(data=serializer.data, safe=False)

 





# GET ve POST @api_views ile
@api_view(http_method_names=['GET', 'POST'])
def stories(request):
    if request.method == 'POST':
        serializer = StoryCreateSerializer(data=request.data, context={'request' : request})  # bizim gonderdiyimiz datani yaz, qebul ele
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
    story_list = Story.objects.all()
    serializer = StorySerializer(story_list, context={'request' : request}, many = True)
    return JsonResponse(data=serializer.data, safe=False)



# PUT ve PATCH @api_views ile
@api_view(http_method_names=['PUT', 'PATCH'])
def story_read_update(request, pk):
    if request.method == 'PUT':
        story = Story.objects.get(pk = pk)
        serializer = StoryCreateSerializer(data=request.data, instance=story, context={'request' : request})  # bizim gonderdiyimiz datani yaz, qebul ele
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
    if request.method == 'PATCH':
        story = Story.objects.get(pk = pk)
        serializer = StoryCreateSerializer(data=request.data, instance=story, partial = True, context={'request' : request})  # bizim gonderdiyimiz datani yaz, qebul ele
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
    