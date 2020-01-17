from modeltranslation.translator import translator, TranslationOptions
from .models import CategoryLink, Link


class LinkTranslationOptions(TranslationOptions):
    fields = ('name', 'description', )


translator.register(Link, LinkTranslationOptions)


class CategoryLinkTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'description_short')


translator.register(CategoryLink, CategoryLinkTranslationOptions)
