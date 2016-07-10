from .forms import EventForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import EventSerializer


class IngestionAPIView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        print request.data
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            event = serializer.create(serializer.validated_data)
            return Response({'result': serializer.data})

        else:
            print 'errors!'
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)