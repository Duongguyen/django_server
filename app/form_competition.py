from django import forms

from app.models_competition import Competition


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['name', 'intro', 'image', 'law', 'statute']