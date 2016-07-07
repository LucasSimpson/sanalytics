from django import forms
from .models import Event, AuthToken

class EventForm(forms.Form):
    auth_token = forms.CharField(max_length=AuthToken.Constants.auth_token_ml)
    event_type = forms.CharField(max_length=Event.Constants.event_type_ml)
    user_token = forms.CharField(max_length=Event.Constants.user_token_ml)
    json_data = forms.CharField(max_length=Event.Constants.json_data_ml)
