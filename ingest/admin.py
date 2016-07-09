from django.contrib import admin
from .models import EventCategory, EventUser, Event, AuthToken

admin.site.register(EventCategory)
admin.site.register(EventUser)
admin.site.register(Event)
admin.site.register(AuthToken)
