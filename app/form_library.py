from django import forms

from app.models_library import LibraryText, LibraryLaw, LibraryReferences


class LibraryTextForm(forms.ModelForm):
    class Meta:
        model = LibraryText
        fields = ['name', 'create_at', 'tag', 'uploaded_file']


class LibraryLawForm(forms.ModelForm):
    class Meta:
        model = LibraryLaw
        fields = ['name', 'create_at', 'tag', 'uploaded_file']


class LibraryReferencesForm(forms.ModelForm):
    class Meta:
        model = LibraryReferences
        fields = ['name', 'create_at', 'tag', 'uploaded_file']
