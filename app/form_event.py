from django import forms

from app.models_event import Events, IntroEvent


class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'intro', 'publication_date', 'address', 'publication_time']


class IntroEventForm(forms.ModelForm):
    class Meta:
        model = IntroEvent
        fields = ['name', 'intro', 'dates', 'address', 'times']
