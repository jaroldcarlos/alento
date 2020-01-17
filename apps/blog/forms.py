from django import forms

from django.utils.translation import gettext_lazy as _
from django_summernote.widgets import SummernoteWidget
from modeltranslation.forms import TranslationModelForm

from .models import BlogPost


class BlogForm(TranslationModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
        }
