from django.urls import path
from blogs.apis.views import (
     categories, 
     tags, 
     stories, 
     comments, 
     story_read_update,
     StoryCreateAPIView,
     CommentCreateAPIView,
     CategoryCreateAPIView,
     StoryRetrieveUpdateDestroyAPIView,
     CategoryRetrieveUpdateDestroyAPIView,
     TagCreateAPIView,
     TagRetrieveUpdateDestroyAPIView
     )


urlpatterns = [
     # path('categories/', categories, name='categories'),
     path('categories/', CategoryCreateAPIView.as_view(), name='categories'),
     # path('tags/', tags, name='tags'),
     path('tags/', TagCreateAPIView.as_view(), name='tags'),
     path('tags/<int:pk>/', TagRetrieveUpdateDestroyAPIView.as_view(), name='tags'),

     # path('stories/', stories, name='stories'),
     path('stories/', StoryCreateAPIView.as_view(), name='stories'),
     # path('comments/', comments, name='comments'),
     path('comments/', CommentCreateAPIView.as_view(), name='comments'),

     # path('stories/<int:pk>/', story_read_update, name='story_read_update'),
     path('stories/<int:pk>/', StoryRetrieveUpdateDestroyAPIView.as_view(), name='story_read_update'),
     path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='categories'),


     
]
