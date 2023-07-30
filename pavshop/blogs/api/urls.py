from django.urls import path
from blogs.api.views import (
    categories, 
    stories, 
    tags, 
    story_read_update,
    StoryCreateAPIView,
    tag_read_update
)



urlpatterns = [
    path('categories/', categories, name='categories'),  # bu demekdir ki, api/categories/ gedende 'categories' function ise dussun, ve views'daki return qaytarsin
    # path('stories/', stories, name='stories'),
    path('stories/', StoryCreateAPIView.as_view(), name='stories'),

    path('tag/', tags, name='tag'),
    path('tag/<int:pk>/', tag_read_update, name='tag_read_update'),
    path('stories/<int:pk>/', story_read_update, name='story_read_update'),
    # path('tags/<int:pk>/', tag_read_update, name='tag_read_update'),

]
