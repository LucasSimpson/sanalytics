from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['domain', 'event_type', 'json_data', 'user_token']
