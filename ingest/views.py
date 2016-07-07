from django.views.generic.base import View
from django.http import JsonResponse

from .forms import EventForm
from .models import Event

# Create your views here.
class IngestionView(View):
    form = EventForm

    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST)
        if form.is_valid():
            print form.cleaned_data
            event = Event()
            event.domain = form.cleaned_data['domain']
            event.event_type = form.cleaned_data['event_type']
            event.json_data = form.cleaned_data['json_data']
            event.user_token = form.cleaned_data['user_token']
            event.save()
            return JsonResponse({'status': 'success'}, status=200)
        else:
            for error in form.errors:
                print error
                print type(error)
                print form [error].errors

            return JsonResponse({'status': 'failure', 'errors': form.errors}, status=400)
