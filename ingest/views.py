from django.views.generic.base import View

# Create your views here.
class IngestionView(View):


    def post(self, request, *args, **kwargs):
        # bind to form, save, return 200 OK
        pass