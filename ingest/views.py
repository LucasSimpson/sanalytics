from django.views.generic.base import View
from django.http import JsonResponse

from .forms import EventForm
from .models import Event
from .helpers import build_event

# Create your views here.
class IngestionView(View):
    form = EventForm

    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST)
        if form.is_valid():
            auth_token = form.cleaned_data['auth_token']
            category = form.cleaned_data['event_category']
            user = form.cleaned_data['event_user']
            json_data = form.cleaned_data['json_data']

            event = build_event(category, user, json_data)

            return JsonResponse({'status': 'success'}, status=200)
        else:
            for error in form.errors:
                print error
                print type(error)
                print form [error].errors

            return JsonResponse({'status': 'failure', 'errors': form.errors}, status=400)
