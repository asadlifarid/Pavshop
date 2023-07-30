from rest_framework import serializers
from products.models import Category, Tag, Brand, PropertyValue, Product, Review

from rest_framework.pagination import PageNumberPagination


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug'
        )



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'slug'
        )



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'slug'
        )



class PropertyValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyValue
        fields = (
            'id',
            'name',
            'property'
        )


# GET
class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.name')
    category = CategorySerializer()
    tag = TagSerializer(many = True)
    brand = BrandSerializer()
    property_values = PropertyValueSerializer(many = True)
    discount = serializers.CharField(source='discount.values')  # queryset qaytarir
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'image',
            'in_stock',
            'quantity',
            'slug',
            'money',
            'brand',
            'category',
            'property_values',
            'discount',
            'tag',
            'small_description',
            'large_description',
        )



# POST
class ProductCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'image',
            'in_stock',
            'quantity',
            'slug',
            'money',
            'brand',
            'category',
            'property_values',
            'discount',
            'tag',
            'small_description',
            'large_description'
        )






class ReviewSerializer(serializers.ModelSerializer):
    # product = serializers.CharField(source='product.title')
    product = ProductSerializer()
    class Meta:
        model = Review
        fields = (
            'id',
            'review',
            'rating',
            'is_active',
            # 'author',
            'author_name',
            'product'
        )



class ReviewCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = (
            'id',
            'review',
            'rating',
            'is_active',
            'author',
            'product'
        )
    
    def validate(self, attrs):
        request = self.context['request']
        attrs['author'] = request.user
        return super().validate(attrs)



# class ProductSetPaginationSerializer(PageNumberPagination):
#     page_size = 100
#     page_query_param = 3
#     max_page_size = 10
