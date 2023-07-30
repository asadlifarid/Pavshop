from rest_framework import serializers
from blogs.models import Category, Story, Tag






# serializer database'dan melumat cekmir, sadece formata salir, ki bu formada gorunsun
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )




# GET
class TagSerializer(serializers.ModelSerializer):
    # stories = StorySerializer(many=True)
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'slug',
        )




# POST
class TagCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'slug',
        )







# GET
class StorySerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.name')
    category = CategorySerializer()
    class Meta:
        model = Story
        fields = (
            'id',
            'title',
            'category',
            'tag',
            # 'author',
            'author_name',
            'slug',
            'description',
            'image',
            'content',
            'is_archive'

        )




# POST
class StoryCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Story
        fields = (
            'id',
            'title',
            'category',
            'tag',
            'author',
            'slug',
            'description',
            'image',
            'content',
            'is_archive'

        )





