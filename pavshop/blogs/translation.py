from modeltranslation.translator import translator, TranslationOptions
from blogs.models import Story, Category, Tag



class StoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Story, StoryTranslationOptions)



class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(Category, CategoryTranslationOptions)



class TagTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(Tag, TagTranslationOptions)