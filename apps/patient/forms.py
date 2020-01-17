from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Patient


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'
