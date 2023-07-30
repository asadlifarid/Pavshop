from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.db.models import Count, Q
from django.core.exceptions import ValidationError

from .models import *
from .forms import CommentForm, CreateStoryForm
from django.forms import Form

from django.urls import reverse_lazy
from django.contrib import messages
import datetime
from datetime import datetime, timedelta, date

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from dateutil import parser
from base.models import AbstractModel
from products.models import Product
# from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout


from authentication import views

from django.contrib.auth import get_user_model, authenticate

User = get_user_model()




# Generic Views importlar
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin  # bu createblog sehifede class uzerine @login_required() qoya bilmirik deye import edirik


# Generic Blog list view
class StoryListView(ListView):
    model = Story   # default name:  model name_list in template istifade edir ozu
    template_name = "blog-list.html"
    context_object_name = "storys"
    ordering = ['created_at']
    paginate_by = 4


    # Category 
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["story_count"] = Category.objects.all()
    #     return context



    def get_queryset(self):
        queryset = super().get_queryset()   #  Story.objects.all() demekdir
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        archive = self.request.GET.get('archive')
        name = self.request.GET.get('search')
        
        if category:
            queryset = queryset.filter(category__name__icontains = category)
        if tag:
            queryset = queryset.filter(tag__name__icontains=tag).all()
        if archive:
            queryset = queryset.filter(updated_at__month=archive).order_by('-updated_at').all()
        if name:
            queryset = queryset.filter(Q(title__icontains=name) | Q(description__icontains=name)).all()

        return queryset
    
    
    # Tags
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["tags"] = Tag.objects.all()
    #     return context


    # Recent Story
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_date"] = datetime.today().month
        context["recent_post"] = Story.objects.filter(updated_at__month=context["current_date"]).order_by('-updated_at')[:3]
        context["blog_archives"] = Story.objects.filter(updated_at__month__lt=context["current_date"]).order_by('-updated_at').dates('updated_at', 'month')
        context["story_count"] = Category.objects.all()
        context["tags"] = Tag.objects.all()
        context["top_rated"] = Product.objects.annotate(Count("reviews"))
        context["rate_list"] = [i for i in context["top_rated"] if float(i.average_rating()) >= 3][:3]
        

        return context
    
    



# About kimi sheifeleri templateview ile yaza bilerik, sadece render edib acir
class CreateStory(LoginRequiredMixin, CreateView):
    template_name = 'create-blog.html'
    form_class = CreateStoryForm
    # success_url = reverse_lazy('blog_list_page')   # 1) bunu da yaza bilerik 2) Modeldeki get_absolute_url override etmek istesek, yene bunu active ede bilerik istediyimiz route'a


    """ 
         get_success_url ona gore yaziriq ki,
         story create edib Submit edende bizi detalli sehifeye aparsin

    """

    """ 
    # biz bunu model'de hell edeceyik ki, her defe pk'sina ve ya slug'na baxmayaq gelib

    def get_success_url(self):
        return reverse_lazy('blog_detail_page', kwargs = {'pk' : self.object.pk})
    """

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    

# class UpdateStory(LoginRequiredMixin, UpdateView):
#     template_name = 'update-blog.html'
#     form_class = CreateStoryForm
#     model = Story


class UpdateStory(LoginRequiredMixin, UpdateView):
    template_name = 'create-blog.html'
    form_class = CreateStoryForm
    model = Story
    # success_url = reverse_lazy('blog_list_page')


    
    


# class SearchStory(ListView):
#     model = Story
#     context_object_name = "storys"
    

#     def search(self):
#         name = self.request.GET.get("search")

#         if name:
#             storys = Story.objects.filter(Q(title__icontains=name) | Q(description__icontains=name)).all() 
#         return storys
            
        

    
    









# Generic Story Detail view
class StoryDetailView(FormMixin, DetailView):
    model = Story
    template_name = 'blog-detail.html'
    context_object_name = "story_details"
    form_class = CommentForm
    # success_url = reverse_lazy('blog_list_page')
    

    def get_success_url(self):
        return reverse_lazy("blog_detail_page", kwargs = {'slug' : self.object.slug})


    def get_queryset(self):
        queryset = super().get_queryset()
        archive = self.request.GET.get('archive')

        
        if archive:
            queryset = queryset.filter(updated_at__month=archive).order_by('-updated_at').all()     
        return queryset





    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["story_count"] = Category.objects.all()
        context["form"] = CommentForm
        context["comments"] = Comment.objects.filter(story__id=self.object.pk)
        context["reviews"] = Comment.objects.filter(story__id=self.object.pk, parent=None).all()
        context["reviews_count"] = context["reviews"].count()
        context["current_date"] = datetime.today().month
        context["recent_post"] = Story.objects.filter(updated_at__month=context["current_date"]).order_by('-updated_at')[:3]
        context["tags"] = Tag.objects.all()
        context["blog_archives"] = Story.objects.filter(updated_at__month__lt=context["current_date"]).dates('updated_at', 'month')
        context["top_stories"] = Story.objects.order_by('-updated_at')[:2]
        return context
    

    



    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # tek bir story qaytarir
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        form.instance.story = self.object
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)





# Create your views here.
def blog_list_page(request):
    categories = Category.objects.all()
    storys = Story.objects.all()
    tags = Tag.objects.all()
   
    
    category = request.GET.get('category')
    tag = request.GET.get('tag')
    name = request.GET.get('search')
    archive = request.GET.get('archive')

    
    # Category ve her categorydeki story sayi
    story_count = Category.objects.annotate(num_storys=Count('stories'))

   
    
    
    # Pagination view 
    """ 'storys' beraber etmeliyik, cunki diger filterleme prosesleri 
         
        storys adli variable'a assign olunub deye

        'page_objects = paginator.page(page)' etsek, filterler islemeyecek   
    """

    page = request.GET.get("page", 1)
    paginator = Paginator(storys, 3)


    try:
        storys = paginator.page(page)
    except PageNotAnInteger:
        storys = paginator.page(1)
    except EmptyPage:
        storys = paginator.page(paginator.num_pages)





    

    # blog_count = Story.objects.filter(is_archive=True)
    # print(blog_count)


    # buradaki archive_count da istifade oluna biler html'de, but sayina gore edirdik sadece
    # archive_count = Story.objects.annotate(num_archives=Count('updated_at')).filter(updated_at__month__range=(1, 12))
    

    # Recent posts ucun
    current_date = datetime.today().month
    recent_post = Story.objects.filter(updated_at__month=current_date).order_by('-updated_at')[:3]


    # Archive posts ucun
    # current_date = datetime.today().month
    print(current_date)

    blog_archives = Story.objects.filter(updated_at__month__lt=current_date).order_by('-updated_at').dates('updated_at', 'month')
    
    counts = Story.objects.dates('updated_at', 'month').order_by('-updated_at')
    print(counts)
    print()
    print(blog_archives)
    

    # bu da isleyir;
    # list_ = []
    # dict_month = {}
    # count = 0
    # for i in blog_count.values():
    #     m = i['updated_at'].month
    #     print(m)

    #     if m not in dict_month.values():
    #         list_.append(i)
    #         dict_month[count] = m
    #         count += 1
        

    # print(dict_month)
    # print(list_)
   #   -   #  -   #




    print("kkkkkkkkkkkkkkkkkkkkkkk")
    



    if category:
        print(category, "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
        storys = Story.objects.filter(category__name__icontains=category).all()
        print('storys burada', storys)
    

    if tag:
        print(tag, 'TTTTTTTTTTTTTTTTTTTTTT')
        storys = Story.objects.filter(tag__name__icontains=tag).all()
        print("tag'a aid story", storys)


    if name:
        print(name)
        storys = Story.objects.filter(Q(title__icontains=name) | Q(description__icontains=name)).all() 
        # print(storys, 'tttttttttttttttttttttttttttttttttttttttttt')

        
    if archive:
        print(archive, 'AAAAAAAAAAAAAAAAAA')
        
        storys = Story.objects.filter(updated_at__month=archive).order_by('-updated_at').all()
        # storys = Story.objects.filter(updated_at__date=parser.parse(archive)).all()
        





    context = {
        'categories':categories,
        'storys':storys,
        'tags':tags,
        'story_count':story_count,
        'category':category,
        'tag':tag,
        'name':name,
        'archive':archive,
        'recent_post':recent_post,
        'blog_archives':blog_archives,
        # 'reviews':reviews,
       
        
        # 'list_':list_,
        
       
    }

    
    
    return render(request, 'blog-list.html', context=context)



# def search_feature(request):

#     storys = Story.objects.all()


#     if request.method == 'POST':
#         search_query = request.POST['search_query']

#         storys = Story.objects.filter(title__contains=search_feature)
#         return render(request, 'blog-list.html', {'query':search_query, 'posts':posts})
#     else:
#         return render(request, 'blog-list.html', {'storys':storys})




# class StoryDetailView(DetailView):
#     model = Story
#     template_name = 'blog-detail.html'


















# Create your views here.

def blog_detail_page(request, id):

    story = get_object_or_404(Story, id=id)
    comments = story.comments.filter(active=True, parent__isnull=True)
    
    form = CommentForm()
    print('form is here -----------')
    if request.method == "POST":
        form = CommentForm(data = request.POST)
        if form.is_valid():
            print('post is valid')
            parent_obj = None

            # get parent comment id from hidden input
            try:
                # id integer e.g. 11
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            
            # if parent_id has been submitted, get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)

            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
                # if parent object exists:
            if parent_obj:
                # create reply comment object
                reply = form.save(commit=False)
                reply.parent = parent_obj
                

            # normal comment
            comment = form.save(commit=False)
            comment.author = request.user
            print(comment.author)
            comment.story = story
            comment.save()
            return redirect(reverse_lazy("blog_detail_page", kwargs={'id':id}))
            

        else:
            form = CommentForm()



    reviews = Comment.objects.filter(story__id=id, parent=None).all()
    reviews_count = reviews.count()
    






    storys = Story.objects.all()
    categorys = Category.objects.all()
    tags = Tag.objects.all()
    story_details = Story.objects.filter(id=id).first()
    # story_detail = Story.objects.get(id=id)
    print('KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK', story_details)
    print()
    # print('detaillllllllllllllllllllllllllll', story_detail)

    # reviews = Comment.objects.all()
    


    category = request.GET.get('category')
    tag = request.GET.get('tag')
    name = request.GET.get('search')


    # category'deki blog sayi
    story_count = Category.objects.annotate(num_storys=Count('stories'))

   
    # Recent post ucun
    recent_post = Story.objects.order_by('-updated_at')[:3]


    # Archives ucun
    current_date = datetime.today().month
    blog_archives = Story.objects.filter(updated_at__month__lt=current_date).dates('updated_at', 'month')

    # You May Like ucun
    top_stories = Story.objects.order_by('-updated_at')[:2]
    print('top-stories!!!!!!!!!!!!!!', top_stories)


    # request'den gelen category ve tag ucun
    if category:
        storys = Story.objects.filter(category__name__icontains=category).all()
        print("story'ler burada FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", storys)

    if tag:
        storys = Story.objects.filter(tag__name__icontains=tag)
        print("tag'lar burada", storys)
        # buarada Story ile Tags modeli ManyToMany field'inde many to many relationship ile connect olduguna gore:   modelin_name__field_name=tag (request'den gelen)
    
    if name:
        storys = Story.objects.filter(title__icontains=name).all()
              
        if name:
            messages.add_message(request, messages.INFO, message='Nothing found! Try browse')
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    


    context = {
        'categorys':categorys,
        'storys':storys,
        'category':category,
        'story_count':story_count,
        'tags':tags,
        'tag':tag,
        'story_details':story_details,
        'recent_post':recent_post,
        'blog_archives':blog_archives,
        'name':name,
        'form':form,
        'reviews':reviews,
        'comments':comments,
        'top_stories':top_stories,
        'reviews_count':reviews_count,
        # 'story':story,

        # 'story-detail':story_detail,

    }
    



    print()
    print(storys)
    # print()
    # print(context)
    # print()
    # print(type(storys))
    # print()
    # print(storys.values())
    # print()
    print(categorys)
    print()
    print(tags)

    print(reviews)
    print(reviews.count())
    for i in reviews:
        print(i.email)


    # for i in storys.values():
    #     print(i,'\n')
    

   
    # print(categorys)
    print()
    # print(context)
    # print()
    # print(type(categorys))
    # print()
    # print(categorys.values())
    # print()
    for i in categorys.values():
        print(i)
    print()

    for i in tags:
        print(i)
    
    
    # storys = Story.objects.all().first()
    # print(storys.query)
    # print(f"title => {storys.title}\ndescription => {storys.description}\ncreated_at => {storys.created_at}\nslug => {storys.slug}\ncategory => {storys.category}")
    
    # print(f'1: {storys[0].title}, 2: {storys[1].description}, 3: {storys[2].created_at}')
    return render(request, 'blog-detail.html', context=context)






@login_required(login_url='login_page')
def create_blog_page(request):

    form = StoryCreateForm()
    if request.method == "POST":
        form = StoryCreateForm(data=request.POST, files=request.FILES)
        print('form is here')
        if form.is_valid():
            print('form is valid !!!!!!')
            blogform = form.save(commit=False)
            blogform.author = request.user
            blogform.save()
            # form.save()
            # storypost.author = request.user
            # storypost.save()
            # obj = form.instance
            # alert = True
            return redirect('blog_list_page')
        else:
            form = StoryCreateForm()

    context = {
        'storyform' : form
    }

    return render(request, 'create-blog.html', context=context)






@login_required(login_url='login_page')
def edit_blog_page(request, id):
    story = get_object_or_404(Story, id=id)

    edit_form = StoryForm(instance=story)
    delete_form = DeleteStoryForm()

    if request.method == "POST":
        if 'edit_story' in request.POST:
            edit_form = StoryForm(request.POST, instance=story)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('blog_list_page')
        if 'delete_story' in request.POST:
            print('yesssss')
            delete_form = DeleteStoryForm(request.POST)
            if delete_form.is_valid():
                print('form is valid 2222222222222')
                story.delete()
                return redirect('blog_list_page')
            

    context = {
        'edit_form' : edit_form,
        'delete_form' : delete_form,
    }

    return render(request, 'edit-blog.html', context=context)

