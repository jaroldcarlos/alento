from django import forms

from apps.expense.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
