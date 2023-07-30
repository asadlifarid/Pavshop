from django.contrib import admin

from .models import *
from base.models import AbstractModel


from modeltranslation.admin import TranslationAdmin



class StoryAdmin(TranslationAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'category', 'slug', 'image', 'image_tag', 'get_tags', 'is_archive')

class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug')


class TagAdmin(TranslationAdmin):
    # fields = ['tag', 'stories', 'slug']
    list_display = ('name', 'slug')   


# class StoryImageAdmin(admin.ModelAdmin):
#     list_display = ('image', 'story', 'created_at')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'story', 'parent', 'created_at', 'message', 'active')



# Register your models here.
admin.site.register(Story, StoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
# admin.site.register(StoryImage, StoryImageAdmin)
admin.site.register(Comment, CommentAdmin)
