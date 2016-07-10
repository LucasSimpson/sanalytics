from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers

from .models import Event, EventCategory, EventUser


class EventSerializer(serializers.Serializer):
    json_data = serializers.CharField()
    user = serializers.CharField()
    category = serializers.CharField()

    def create(self, data):
        c = data.get('event_category', 'uncategorized')
        try:
            category = EventCategory.objects.get(category=c)
        except ObjectDoesNotExist:
            category = EventCategory()
            category.category = c
            category.save()

        u = data.get('event_user', 'anon')
        try:
            user = EventUser.objects.get(uuid=u)
        except ObjectDoesNotExist:
            user = EventUser()
            user.uuid = u
            user.save()

        event = Event()
        event.json_data = data.get('json_data', '')
        event.category = category
        event.user = user
        event.save()

        return event