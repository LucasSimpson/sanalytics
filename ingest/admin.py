from django.contrib import admin
from .models import Event, AuthToken

admin.site.register(Event)
admin.site.register(AuthToken)
