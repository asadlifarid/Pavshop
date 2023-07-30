from django.urls import path

from blogs.views import blog_list_page, blog_detail_page, create_blog_page, edit_blog_page, StoryListView, StoryDetailView, CreateStory, UpdateStory




urlpatterns = [
    # path('<slug:slug>', views.blog_detail_page, name='blog_detail_page'),
    # path('blog-detail/<int:id>/', blog_detail_page, name='blog_detail_page'),
    path('blog-detail/<str:slug>/', StoryDetailView.as_view(), name='blog_detail_page'),

    # path('blog-list/', views.blog_list_page, name='blog_list_page'),
    path('blog-list/', StoryListView.as_view(), name='blog_list_page'),

    # path('edit-blog/<int:id>/edit/', edit_blog_page, name='edit_blog_page'),
    # path('update-blog/<int:pk>/', UpdateStory.as_view(), name='update_blog_page'),
    path('update-blog/<int:pk>/', UpdateStory.as_view(), name='update_blog_page'),


    # path('create-blogs/', create_blog_page, name='create_blog_page'),
    path('create-blog/',  CreateStory.as_view(), name='create_blog_page'),


]
