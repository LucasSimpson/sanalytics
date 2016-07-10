from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers

from .models import Event, EventCategory, EventUser


class EventUserNameSerializer(serializers.Field):
    def to_representation(self, event_user):
        return event_user.uuid

    def to_internal_value(self, data):
        return EventUser.objects.get(uuid=data)


class EventCategoryNameSerializer(serializers.Field):
    def to_representation(self, event_category):
        return event_category.category

    def to_internal_value(self, data):
        return EventCategory.objects.get(category=data)


class EventSerializer(serializers.Serializer):
    json_data = serializers.CharField()

    def create(self, data):
        print 'in create'
        c = data.get('event_category', 'uncategorized')
        u = data.get('event_user', 'anon')

        try:
            category = EventCategory.objects.get(category=c)
        except ObjectDoesNotExist:
            category = EventCategory()
            category.category = category
            category.save()

        try:
            user = EventUser.objects.get(uuid=u)
        except ObjectDoesNotExist:
            user = EventUser()
            user.uuid = user
            user.save()


        event = Event()
        event.json_data = data.get('json_data', '')
        event.category = category
        event.user = user
        event.save()

        return ''