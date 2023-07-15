from django import forms

from app.models_partner import Partner


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['name', 'address', 'image', 'phone', 'social_network', 'email']
