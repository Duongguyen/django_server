from django import forms

from app.models_intro import Greeting, IntroFederation


class GreetingsForm(forms.ModelForm):
    class Meta:
        model = Greeting
        fields = ['title', 'description', 'image']


class IntroFederationForm(forms.ModelForm):
    class Meta:
        model = IntroFederation
        fields = ['title', 'description', 'image']


