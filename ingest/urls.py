from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = patterns ('',
    url(r'^$', csrf_exempt(views.IngestionView.as_view()), name='ingest'),
)