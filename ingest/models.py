from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class EventUser(models.Model):
    class Constants:
        uuid_ml = 36

    uuid = models.CharField(primary_key=True, max_length=Constants.uuid_ml)

    def __str__(self):
        return self.uuid


class EventCategory(models.Model):
    class Constants:
        category_ml = 128

    category = models.CharField(primary_key=True, max_length=Constants.category_ml)

    def __str__(self):
        return self.category

class Event(models.Model):
    class Constants:
        json_data_ml = 1024

    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(EventUser, on_delete=models.CASCADE)
    json_data = models.CharField(max_length=Constants.json_data_ml)

    def __str__(self):
        return self.category.__str__() + '@' + self.timestamp.strftime("%A, %d. %B %Y %I:%M%p") + ' by ' + self.user.__str__()



class AuthToken(models.Model):
    class Constants:
        auth_token_ml = 64

    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    auth_token = models.CharField(max_length=Constants.auth_token_ml, unique=True)