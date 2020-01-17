from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'
