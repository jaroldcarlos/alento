from django.contrib import admin

from modeltranslation.admin import TranslationAdmin
from django_summernote.admin import SummernoteModelAdmin
from .models import CategoryService, Service, SpecialisedUnit


class CategoryServiceAdmin(TranslationAdmin, SummernoteModelAdmin):
    summernote_fields = ('description')


class ServiceAdmin(TranslationAdmin, SummernoteModelAdmin):
    summernote_fields = ('description')


class SpecialisedUnitAdmin(TranslationAdmin):
    pass


admin.site.register(CategoryService, CategoryServiceAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(SpecialisedUnit)
