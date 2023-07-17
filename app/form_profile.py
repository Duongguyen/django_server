from django import forms

from app.models_profile import Athlete, Coach, Referee


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['fullname', 'object', 'sex', 'archie', 'social_network', 'date_of_birth', 'home_live', 'image', 'career']


class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ['fullname', 'object', 'sex', 'archie', 'social_network', 'date_of_birth', 'home_live', 'image', 'career']


class RefereeForm(forms.ModelForm):
    class Meta:
        model = Referee
        fields = ['fullname', 'object', 'sex', 'archie', 'social_network', 'date_of_birth', 'home_live', 'image', 'career']




