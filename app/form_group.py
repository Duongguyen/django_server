from django import forms

from .models_group import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name_group', 'subject', 'image', 'year', 'social_network', 'intro', 'achier']

