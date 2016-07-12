from rest_framework.generics import ListAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework import status

from .serializers import EventSerializer
from .models import Event


class IngestionAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = EventSerializer

    queryset = Event.objects.all()



    def post(self, request):
        serializer = IngestionAPIView.serializer_class(data=request.data)

        if serializer.is_valid():
            event = serializer.create(serializer.validated_data)
            return Response({'result': serializer.data})

        else:
            print 'errors!'
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)