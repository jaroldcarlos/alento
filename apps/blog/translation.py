from modeltranslation.translator import translator, TranslationOptions
from .models import BlogPost, BlogCategory


class BlogPostModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'description_short', 'subtitle', 'slug')


class BlogCategoryModelTranslationOptions(TranslationOptions):
    fields = ('name', 'description_short')


translator.register(BlogPost, BlogPostModelTranslationOptions)
translator.register(BlogCategory, BlogCategoryModelTranslationOptions)
