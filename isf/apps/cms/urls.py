from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from cms.views import *

# orzubalskydotcom application
urlpatterns = patterns('cms.views',
    # url(r'news/(?P<slug>[0-9A-Za-z\-]+)$', PostDetail.as_view(), name='post-detail'),
    url(r'$', TemplateView.as_view(template_name="home.html"), name='home'),
)
