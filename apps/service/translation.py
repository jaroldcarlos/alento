from modeltranslation.translator import translator, TranslationOptions
from .models import Service, CategoryService, SpecialisedUnit


class ServiceModelTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'description_short')


class CategoryServiceModelTranslationOptions(TranslationOptions):
    fields = ('name', 'description_short', 'description')


class SpecialisedUnitModelTranslationOptions(TranslationOptions):
    fields = ('name', )


translator.register(Service, ServiceModelTranslationOptions)
translator.register(CategoryService, CategoryServiceModelTranslationOptions)
translator.register(SpecialisedUnit, SpecialisedUnitModelTranslationOptions)
