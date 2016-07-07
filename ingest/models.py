from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Event(models.Model):
    class Constants:
        event_type_ml = 64
        user_token_ml = 64
        json_data_ml = 1024

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=Constants.event_type_ml)
    user_token = models.CharField(max_length=Constants.user_token_ml, default='anon')
    json_data = models.CharField(max_length=Constants.json_data_ml)

    def __str__(self):
        return self.domain + '::' + self.event_type + '@' + self.timestamp.strftime("%A, %d. %B %Y %I:%M%p") + ' by ' + self.user_token

class AuthToken(models.Model):
    class Constants:
        auth_token_ml = 64

    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    auth_token = models.CharField(max_length=Constants.auth_token_ml, unique=True)