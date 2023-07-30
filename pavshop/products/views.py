from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
import requests
from django.db.models import Count, Q

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# from django.db.models import Q

from .models import *
from .forms import ReviewForm
from django.forms import Form

from django.urls import reverse_lazy
from base.models import AbstractModel

from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

# query = urllib.parse.quote_plus(request)




# Generic Views importlar
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin


# Celery task importlar
from products.tasks import export_data



class ProductListView(ListView):
    model = Product
    template_name = 'product-list.html'
    context_object_name = 'products'
    ordering = ['created_at']
    paginate_by = 6




    def get_queryset(self):
        queryset = super().get_queryset()     # Products.objects.all() demekdir
        category = self.request.GET.get('category')
        color = self.request.GET.get('color')
        brand = self.request.GET.get('brand')
        tag = self.request.GET.get('tag')
        name = self.request.GET.get('search')
        min_price = self.request.GET.get('min')
        max_price = self.request.GET.get('max')

        if category:
            queryset = queryset.filter(category__name__icontains=category).all()
        if color:
            queryset = queryset.filter(property_values__name__icontains=color).all()
        if brand:
            queryset = queryset.filter(brand__name=brand).all()
        if tag:
            queryset = queryset.filter(tag__name__icontains=tag).all()
        if name:
            queryset = queryset.filter(title__icontains=name).all()
        if min_price and max_price:
            queryset = queryset.filter(money__gte=min_price) & Product.objects.filter(money__lte=max_price)

        return queryset
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["colors"] = PropertyValue.objects.all()
        context["brands"] = Brand.objects.all()
        context["product_count"] = Category.objects.annotate(num_products=Count('products'))
        # context["product_count"] = Category.objects.all()  yaza bilerik, html'de .count ile sayi gostererik o zaman
        context["tags"] = Tag.objects.all()
        context["top_rated"] = Product.objects.annotate(Count("reviews"))
        context["rate_list"] = [i for i in context["top_rated"] if float(i.average_rating()) >= 3][:3]
        
        return context
        






class ProductDetailView(FormMixin, DetailView):
    model = Product
    template_name = 'product-detail.html'
    context_object_name = 'products'
    form_class = ReviewForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    # success_url = reverse_lazy('product_list_page')
    
    

    def get_success_url(self):
        return reverse_lazy("product_detail_page", kwargs={"slug": self.object.slug})
        # return reverse_lazy("product_detail_page", kwargs = {'pk' : self.object.pk})


 

    def get_queryset(self):
        queryset = super().get_queryset()      # Product.objects.all()  demekdir
        color = self.request.GET.get('color')

        if color:
            queryset = queryset.filter(id=self.object.pk).first()
        return queryset




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_products"] = Product.objects.filter(money__gte=100).all()
        context["reviews"] = Review.objects.filter(product__id=self.object.pk)
        context["discounts"] = Discount.objects.get(name='Summer')
        print(context["discounts"])
        # reviews = product.reviews.filter(is_active=True)

        context["comments"] = Review.objects.filter(product__id=self.object.pk).order_by('created_at')
        context["comments_count"] = context["comments"].count()
        context["images"] = ProductImages.objects.filter(product__id=self.object.pk).all()
        context["form"] = ReviewForm
        context["top_rated"] = Product.objects.annotate(Count("reviews"))
        context["rate_list"] = [i for i in context["top_rated"] if float(i.average_rating()) >= 3][:3]
        return context
        


    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # tek bir product qaytarir
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        form.instance.product = self.object
        form.instance.author = self.request.user
        # form.instance.rating = self.object
        form.save()
        return super().form_valid(form)




    
    
def export_view(request):
    export_data.delay()
    return HttpResponse('success')
    






# Create your views here.
def product_list_page(request):
    # colors = Color.objects.all()
    colors = PropertyValue.objects.all()

    brands = Brand.objects.all()
    cat = Category.objects.all()
    tags = Tag.objects.all()
    products = Product.objects.all()

    # variants = Variant.objects.all()
    # print(variants)
    # values = Product.objects.values()
    # # print('values', values)
    # # list_ = []
    # # print(Product.objects.all().values())
    # versions = ProductVersion.objects.values()
    
    

    min_price = request.GET.get('min')
    max_price = request.GET.get('max')

    color = request.GET.get('color')
    brand = request.GET.get('brand')
    category = request.GET.get('category')
    tag = request.GET.get('tag')

    name = request.GET.get('search')

    # # product_count = Category.count_cat()
    # # product_count = Product.count_product()
    # # print(product_count)
    # product_count = Product.objects.annotate(category=Count(category))
    # # product_count = Product.objects.filter(category__name='Furniture').count()

    # # product_count = Product.objects.annotate(items_count=Count(''))


    product_count = Category.objects.annotate(num_products=Count('products'))
    # product_count = Category.objects.annotate(num_products=Count('variants'))
    



    for product in product_count:
        print(product.name, product.num_products)

    # # counts = Product.objects.all()
    # # counts = Product.objects.filter(category__name=category).all().count()

    # # query = urllib.parse.quote_plus('category')
    # # print(min_price, max_price)
    # # product_images = ProductImages.objects.all()



    # Pagination view
    page = request.GET.get("page", 1)
    paginator = Paginator(products, 6)


    try:
        products = paginator.page(page)
        # variants = paginator.page(page)

    except PageNotAnInteger:
        products = paginator.page(1)
        # variants = paginator.page(1)

    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        # variants = paginator.page(paginator.num_pages)





    if min_price and max_price:
        # products = Product.objects.filter(price__gte=min_price, price__lte=max_price)
        products = Product.objects.filter(money__gte=min_price) & Product.objects.filter(money__lte=max_price)
        # variants = Variant.objects.filter(money__gte=min_price) & Variant.objects.filter(money__lte=max_price)

        print('If -deki body', products)
        print()

    # if color:
    #     products = Color.objects.filter(name=color).all()
    #     print(products, '1111111111111111')

    if color:
        print(color, 'TTTTTTTTTTTTTTTTTTTTTT')
        products = Product.objects.filter(property_values__name__icontains=color).all()
        # variants = Variant.objects.filter(color__name__icontains=color).all()

        print("tag'a aid story", products)

    if brand:
        products = Product.objects.filter(brand__name=brand).all()
        # variants = Variant.objects.filter(product__brand__name=brand).all()

        

    if category:
        products = Product.objects.filter(category__name__icontains=category).all()
        # variants = Variant.objects.filter(category__name__icontains=category).all()

        # counts = Product.objects.filter(category__name=category).all().count()
        # print(counts)
        print("category'ler burda: ", category)

    
    if name:
        print(name)
        products = Product.objects.filter(title__icontains=name).all()
        # variants = Variant.objects.filter(title__icontains=name).all()

        print(products, 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyy')

    if tag:
        print(tag, 'TTTTTTTTTTTTTTTTTTTTTT')
        products = Product.objects.filter(tag__name__icontains=tag).all()
        # variants = Variant.objects.filter(tag__name__icontains=tag).all()

        print("tag'a aid story", products)


    # # if values:
    # #     products = Product.objects.filter(category__name__icontains=title).all().count()
    # #     for i in products.values():
    # #         list_.append(i['category_id'])
    # #     print(list_.count(i['category_id']))



    # # if values:
    # #     products = Product.objects.filter(id__in=Category.objects.values()[0]['id']).all().count()
    # #     print('count', products)

    # # if counts:
    # #     counts_ = Product.objects.filter(category__name=category).all().count()
    

    context = {
        'colors':colors,
        'brands':brands,
        'cat':cat,
        'tags':tags,
        'products':products,
        'min_price':min_price,
        'max_price':max_price,
        'color':color,
        'brand':brand,
        'category':category,
        'tag':tag,
        # 'values':values,
        'product_count':product_count,
        'name':name,
        # 'variants':variants,




        # 'versions':versions,
        # 'product':product,
        # 'list_':list_,
        # 'counts':counts,
        # 'counts_':counts_,
        # 'product_images':product_images,
    }   



    # # print(colors)
    # # print()
    # # print(context)
    # # print()
    # # print(type(colors))
    # # print()
    # # print(colors.values())
    # # print()
    # print('brands', brands)
    # # print()
    # print('brand values', brands.values())
    # # print()
    # print(categories)
    # # print()
    # print(categories.values())
    # # print()
    # print('tags', tags)
    # # print()
    # print('tags values ', tags.values())
    # # print()
    # print(products)
    # # print()
    # # print(products.values())
    # # print()
    
    # # # print(product_images)
    # # # print()
    # # # print(product_images.values())

    # for i in colors.values():
    #     print(i)

    # # print()

    # for i in brands.values():
    #     print(i)
    
    # # print()

    # for i in categories.values():
    #     print(i)
    
    # # print()

    # # for i in tag.values():
    # #     print(i)
    # # print()

    # # for i in products.values():
    # #     print(i)
    # # print()
    

    # # list_ = []
    # # for i in products.values():
    # #     print(i['title'], ' ', i['category_id'])
    # #     list_.append(i['category_id'])

    # # # print(list_)
    # # # print(list_.count(i['category_id']))

    # # # for i in product_images.values():
    # # #     print(i)

    return render(request, 'product-list.html', context=context)





# Create your views here.
def product_detail_page(request, id):

    product = get_object_or_404(Product, id=id)
    reviews = product.reviews.filter(is_active=True)

    form = ReviewForm()
    print("form is here -------")
    if request.method == "POST":
        form = ReviewForm(data = request.POST)
        if form.is_valid():
            print("form is valid!!!!!!")
            review = form.save(commit=False)
            review.author = request.user
            print(review.author)
            # print(review.author.get_avatar)
            review.product = product
            review.save()
            return redirect(reverse_lazy("product_detail_page", kwargs={'id':id}))
        else:
            form = ReviewForm()

   

    comments = Review.objects.filter(product_id=id).order_by('created_at')
    comments_count = comments.count()



    # all_products = Product.objects.all()[5:10]
    # all_products = Product.objects.filter(money__gte=100).all()
  
    all_products = Product.objects.filter(money__gte=100).all()
    categories = Category.objects.all()
    products = Product.objects.filter(id=id).first()
    print(products, 'TTTTTTTTTTTTTTTTTT')


    images = ProductImages.objects.filter(product__id=id).all()
    
    color = request.GET.get('color')
    
    if color:
        print(color)
        # products = Product.objects.filter(color__name__icontains=color)
        products = Product.objects.filter(id=id).first()

        print(products, 'tttttttttt')



# shell result

# >>> x = Product.objects.filter(id=1).first() 
# >>> x.property_values
# <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x000001F5F66EC880>
# >>> x.property_values.all()
# <QuerySet [<PropertyValue: White>]>
# >>>




    
    
    

    context = {
        'all_products':all_products,
        'categories':categories,
        'images':images,
        'products':products,
        'form':form,
        'comments_count':comments_count,
        # 'product':product,
        'reviews':reviews,
        
        # 'variants':variants,
        'color':color,
        # 'values':values,
        # 'pro':pro,
        # 'colours':colours,
        
        # 'categorys_':categorys_,
        # 'brands_':brands_,
        
    }
    
    # print()
    # # print(images)
    # # print()
    # print(variants)
    # # print()
    # # print(brands)
    # # print()
    # print(categories)
    # # print()
    # # print(colors)
    # # print(categorys_)
    # print()
    # # print(brands_)


    # print()
    # print("Product Images")
    # for i in images.values():
    #     print(i)
    # print()
    
    # # for i in brands_:
    # #     print(i)

    # # print("Product Variants")
    # # for i in variants:
    # #     print(i)
    # #     print(i.brand.name)
    # # print()

    # # print("Brands")
    # # for i in brands.values():
    # #     print(i)
    # # print()
    
    # # print("Categorys")
    # # for i in categorys:
    # #     print(i.name)
    # #     # print(i.name)
    # # print()
    
    # # print("Product -> category'ye catmaq ucun:")
    # # for i in categorys_:
    # #     print(i.category.name)

    
    return render(request, 'product-detail.html', context=context)




