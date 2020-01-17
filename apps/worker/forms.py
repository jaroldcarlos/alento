from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Worker


class WorkerForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    dni = forms.CharField(max_length=9)
    is_staff = forms.BooleanField(required=False)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = Worker
        fields = '__all__'
