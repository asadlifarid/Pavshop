from modeltranslation.translator import translator, TranslationOptions
from products.models import Product, Category, Tag


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'small_description')

translator.register(Product, ProductTranslationOptions)



class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(Category, CategoryTranslationOptions)



class TagTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(Tag, TagTranslationOptions)