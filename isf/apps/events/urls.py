from django.conf.urls import patterns, url
from events.views import *

# orzubalskydotcom application
urlpatterns = patterns('events.views',
    url(r'(?P<slug>[0-9A-Za-z\-]+)$', 'event_detail', name='event-detail'),
    url(r'$', 'home', name='home'),
)
