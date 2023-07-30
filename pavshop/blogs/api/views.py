from blogs.models import Category, Story, Tag
from django.http import JsonResponse  # return render evezine, return jsonresponse deyeceyik, ki gelen deyerler json formatinda qayitsin
from blogs.api.serializers import (
    CategorySerializer, 
    StorySerializer, 
    TagSerializer, 
    StoryCreateSerializer,
    TagCreateSerializer
    )


from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView




# @api_view(http_method_names=['GET', 'POST'])
# def tags(request):
#     tag_list = Tag.objects.all()
#     serializer = TagSerializer(tag_list, many=True)
#     return JsonResponse(data=serializer.data, safe=False)





def categories(request):
    category_list = Category.objects.all()  # 1)category'lerin hamisini ceksin
    # category_dict_list = []  # 2) bos list yaradiriq, amma icine dictionary gonderecem, json formati kimi, yeni bize list qayidir, icinde dict olur
    # for cat in category_list:
    #     category_dict_list.append({
    #         'cat_id' : cat.id,
    #         'name' : cat.name
    #     })
    serializer = CategorySerializer(category_list, many = True)
    return JsonResponse(data=serializer.data, safe=False)





# class StoryCreateAPIView(ListAPIView):
#     serializer_class = StoryCreateSerializer
#     queryset = Story.objects.all()


# GET vs POST bir yerde generic API
class StoryCreateAPIView(ListCreateAPIView):
    serializer_class = StoryCreateSerializer
    queryset = Story.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StorySerializer
        return self.serializer_class





@api_view(http_method_names=['GET', 'POST'])
def stories(request):
    if request.method == 'POST':
        serializer = StoryCreateSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
        
    story_list = Story.objects.all()
    serializer = StorySerializer(story_list, context={'request':request}, many = True)
    return JsonResponse(data=serializer.data, safe=False)




@api_view(http_method_names=['PUT', 'PATCH'])
def story_read_update(request, pk):
    if request.method == 'PUT':
        story = Story.objects.get(pk = pk)
        serializer = StoryCreateSerializer(data=request.data, instance = story, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
        
    if request.method == 'PATCH':
        story = Story.objects.get(pk = pk)
        serializer = StoryCreateSerializer(data=request.data, instance = story, partial = True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
        






@api_view(http_method_names=['GET', 'POST'])
def tags(request):
    if request.method == 'POST':
        serializer = TagCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)

    tag_list = Tag.objects.all()
    serializer = TagSerializer(tag_list, many=True)
    return JsonResponse(data=serializer.data, safe=False)




@api_view(http_method_names=['PUT', 'PATCH'])
def tag_read_update(request, pk):
    if request.method == 'PUT':
        tag = Tag.objects.get(pk = pk)
        
        serializer = TagCreateSerializer(data=request.data, instance = tag, context={'request' : request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)

    if request.method == 'PATCH':
        tag = Tag.objects.get(pk = pk)
        serializer = TagCreateSerializer(data=request.data, instance = tag, partial = True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)



