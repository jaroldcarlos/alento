from django.contrib import admin

from django.utils.translation import ugettext as _

from modeltranslation.admin import TranslationAdmin
from django_summernote.admin import SummernoteModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import CategoryLink, Link, Contact_us, Social


class CategoryLinkAdmin(TranslationAdmin, SummernoteModelAdmin):

    summernote_fields = ('description', )
    list_display = ('name',)
    list_display_links = ('name',)
    fieldsets = (
        (_('Information'),
            {
                'fields': ('name', 'description', 'description_short', 'hook'),
        }),
    )


class LinkAdmin(TranslationAdmin, DjangoMpttAdmin):
    # readonly_fields = ["tree_id", ]
    item_label_field_name = 'full_display_admin'
    fieldsets = (
        (_('hook'),
            {
                'fields': ('hook', ),
        }),
        (_('parent'),
            {
                'fields': ('parent', ),
        }),
        (_('text'),
            {
                'fields': ('name', 'description', 'url', 'icon', 'color'),
        }),
    )


class SocialAdmin(admin.ModelAdmin):

    list_display = ('name', 'active_status')
    list_display_links = ('name', )
    fieldsets = (
        (_('active'),
            {
                'fields': ('active_status', ),
        }),
        (_('Information'),
            {
                'fields': ('name', 'url', ),
        }),
    )


admin.site.register(CategoryLink, CategoryLinkAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Contact_us)
admin.site.register(Social, SocialAdmin)
