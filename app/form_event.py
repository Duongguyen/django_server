from django import forms

from app.models_event import Events


class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'intro', 'publication_date', 'address', 'publication_time']
