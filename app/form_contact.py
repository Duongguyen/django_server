from django import forms

from .models_contact import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'address', 'phone']