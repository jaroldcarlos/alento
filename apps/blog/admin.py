from django.contrib import admin

from modeltranslation.admin import TranslationAdmin
from django_summernote.admin import SummernoteModelAdmin

from .models import BlogPost, BlogCategory


class BlogCategoryAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ('active_status', 'name', 'description_short',)
    list_display_links = ('active_status', 'name')
    fieldsets = (
        ('Active', {
            'fields': ('active_status',),
        }),
        ('Data', {
            'fields': ('name', 'description_short'),
        }),
        ('imagen', {
            'fields': ('image', ),
        }),
    )


class BlogPostAdmin(TranslationAdmin, SummernoteModelAdmin):
    summernote_fields = ('description')
    list_display = ('active_status', 'category', 'title')
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('active_status', 'title')
    fieldsets = (
        ('Active', {
            'fields': ('active_status','date_active_ini', 'date_active_end'),
        }),
        ('Data', {
            'fields': ('author', 'category', 'title',  'description_short', 'icon', 'slug'),
        }),
        ('imagen', {
            'fields': ('image',),
        }),
        ('subtitle', {
            'fields': ('subtitle', 'description'),
        }),
    )


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
