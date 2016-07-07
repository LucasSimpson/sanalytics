from __future__ import unicode_literals

from django.db import models

class Event(models.Model):
    domain = models.URLField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=64)
    user_token = models.CharField(max_length=64, default='anon')
    json_data = models.CharField(max_length=1024)

    def __str__(self):
        return self.domain + '::' + self.event_type + '@' + self.timestamp.strftime("%A, %d. %B %Y %I:%M%p") + ' by ' + self.user_token