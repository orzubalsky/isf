from django.conf.urls import patterns, url
from letters.views import *

# orzubalskydotcom application
urlpatterns = patterns('letters.views',
    url(r'(?P<slug>[0-9A-Za-z\-]+)$', 'letter_detail', name='letter-detail'),
    # url(r'$', LetterList.as_view(), name='letter-list'),
)
