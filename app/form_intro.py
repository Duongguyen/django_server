from django import forms

from app.models_intro import Greeting, IntroFederation, IntroEvolution, IntroMission


class GreetingsForm(forms.ModelForm):
    class Meta:
        model = Greeting
        fields = ['title', 'description', 'image']


class IntroFederationForm(forms.ModelForm):
    class Meta:
        model = IntroFederation
        fields = ['title', 'description', 'image']


class IntroEvolutionForm(forms.ModelForm):
    class Meta:
        model = IntroEvolution
        fields = ['title', 'description', 'image']


class IntroMissionForm(forms.ModelForm):
    class Meta:
        model = IntroMission
        fields = ['title', 'description', 'image']

