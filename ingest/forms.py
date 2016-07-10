from django import forms
from .models import EventCategory, EventUser, Event, AuthToken

class EventForm(forms.Form):
    auth_token = forms.CharField(max_length=AuthToken.Constants.auth_token_ml)
    category = forms.CharField(max_length=EventCategory.Constants.category_ml)
    user = forms.CharField(max_length=EventUser.Constants.uuid_ml)
    json_data = forms.CharField(max_length=Event.Constants.json_data_ml)
