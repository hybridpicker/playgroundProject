from django.utils.translation import gettext as _
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    from_email = forms.EmailField(label="E-Mailadresse", max_length=100, required=True)
    message = forms.CharField(label="Nachricht",widget=forms.Textarea, required=False)
