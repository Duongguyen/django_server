from django import forms

from app.models_intro import Greeting


class GreetingsForm(forms.ModelForm):
    class Meta:
        model = Greeting
        fields = ['title', 'description', 'image']


