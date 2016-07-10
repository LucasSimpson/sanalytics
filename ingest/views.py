from .forms import EventForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import EventSerializer


class IngestionAPIView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        form = EventForm(request.POST)
        serializer = EventSerializer(data=request.POST)

        if serializer.is_valid():
            event = serializer.create(serializer.validated_data)
            return Response({'status': 'success'})

        else:
            print 'errors!'
            return Response({'status': 'failure', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)