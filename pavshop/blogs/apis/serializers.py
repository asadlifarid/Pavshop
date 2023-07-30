from rest_framework import serializers
from blogs.models import Category, Tag, Story, Comment


# modelin adina uygun serializer yaradiriq
# database'dan melumat cekmir, bir formata - JSON formatina salir, ekranda bu formatda duzsun, views'dan gonderecyik icerisine melumati
class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
        )
        ref_name = 'Category Blog'



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'slug',
        )
        ref_name = 'Tag Blog'


# GET
class StorySerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.name')
    category = CategorySerializer()  # serializer icinde diger serializer gostersin, yeni obyekt olaraq gostersin, id olaraq yox
    tag = TagSerializer(many = True)
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
            'image',
            'is_archive',
            'description',
            'content',
        )




# POST 
class StoryCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
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
            'image',
            'is_archive',
            'description',
            'content',
        )

    def validate(self, attrs):
        request = self.context['request']
        attrs['author'] = request.user
        return super().validate(attrs)












class CommentSerializer(serializers.ModelSerializer):
    # story = serializers.CharField(source='story.title')
    story = StorySerializer()
    class Meta:
        model = Comment
        fields = (
            'message',
            'active',
            # 'author',
            'author_name',
            'story',
            'parent'

        )



class CommentCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = (
            'message',
            'active',
            'author',
            'story',
            'parent'

        )

    def validate(self, attrs):
        request = self.context['request']
        attrs['author'] = request.user
        return super().validate(attrs)