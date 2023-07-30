from rest_framework import serializers
from products.models import Category, Brand, Product, Tag, Property, PropertyValue, ProductImages



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
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




class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = (
            'id',
            'name'
        )



# GET
class PropertyValueSerializer(serializers.ModelSerializer):
    # property = serializers.CharField(source='property.name')
    property = PropertySerializer()
    class Meta:
        model = PropertyValue
        fields = (
            'id',
            'name',
            'property'
        )




# POST
class PropertyValueCreateSerializer(serializers.ModelSerializer):
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
    # property_values = serializers.CharField(source='property_values.all')   -> bu queryset qaytarir
    # property_values = serializers.CharField(source='property_values.name')  -> null qaytarir
    property_values = PropertyValueSerializer(many=True)
    category = CategorySerializer()
    brand = BrandSerializer()
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'small_description',
            'large_description',
            'image',
            'in_stock',
            'quantity',
            'money',
            'slug',
            'category',
            'brand',
            'property_values',
            'discount'

        )



# POST
class ProductCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)  # sadece oxumaq ucundur, create edende ozu yaradir, required olunmur
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'small_description',
            'large_description',
            'image',
            'in_stock',
            'quantity',
            'money',
            'slug',
            'category',
            'brand',
            'property_values',
            'discount'

        )








# GET 
class TagSerializer(serializers.ModelSerializer):
    # products = serializers.CharField(source='products.title')
    products = ProductSerializer(many=True)
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'slug',
            'products'
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
            'products'
        )





# GET
class ProductImagesSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = ProductImages
        fields = (
            'id',
            'image',
            'product'
        )



# POST
class ProductImagesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = (
            'id',
            'image',
            'product'
        )

