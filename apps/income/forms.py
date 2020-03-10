from django import forms

from apps.income.models import Income

from django.conf import settings

class IncomeForm(forms.ModelForm):
    class Meta:
        date_payment = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
        model = Income
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(IncomeForm, self).__init__(*args, **kwargs)
