from django.contrib import admin
from .models import Income


class IncomeAdmin(admin.ModelAdmin):

    list_display = ('date', 'invoice_number', 'total')
    list_display_links = ('invoice_number',)
    list_filter = ('date', )


admin.site.register(Income, IncomeAdmin)
