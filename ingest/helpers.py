from django.core.exceptions import ObjectDoesNotExist
from .models import Event, EventCategory, EventUser

# creates an event, associating it with the correct category/user.
# creates the category/user models in db if they dont exist
def build_event(category, user, json_data):
    e = Event()
    e.json_data = json_data

    try:
        c = EventCategory.objects.get(category=category)
    except ObjectDoesNotExist:
        c = EventCategory()
        c.category = category
        c.save()

    try:
        u = EventUser.objects.get(uuid=user)
    except ObjectDoesNotExist:
        u = EventUser()
        u.uuid = user
        u.save()

    e.category = c
    e.user = u
    e.save()

    return e