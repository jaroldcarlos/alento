from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    telephone = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea, required=True)
