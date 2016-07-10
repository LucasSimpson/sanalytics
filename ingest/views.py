from django.views.generic.base import View
from django.http import JsonResponse

from .forms import EventForm
from .models import Event
from .helpers import build_event


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions

from .serializers import EventSerializer

# Create your views here.
class IngestionView(View):
    form = EventForm

    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST)
        if form.is_valid():
            auth_token = form.cleaned_data['auth_token']
            category = form.cleaned_data['category']
            user = form.cleaned_data['user']
            json_data = form.cleaned_data['json_data']

            event = build_event(category, user, json_data)

            return JsonResponse({'status': 'success'}, status=200)
        else:
            for error in form.errors:
                print error
                print type(error)
                print form [error].errors

            return JsonResponse({'status': 'failure', 'errors': form.errors}, status=400)


class IngestionAPIView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        form = EventForm(request.POST)
        serializer = EventSerializer(data=request.POST)

        if serializer.is_valid():
            print 'got here'
        if serializer.is_valid():
            event = serializer.create(serializer.validated_data)
            return Response({'status': 'success'})
        else:
            print 'errors!'
            return Response({'status': 'failure', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)