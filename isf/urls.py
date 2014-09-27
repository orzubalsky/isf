from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps import FlatPageSitemap
from cms.sitemaps import PostSitemap, StaticViewSitemap
from events.sitemaps import EventSitemap
from letters.sitemaps import LetterSitemap
from django.conf import settings
from filebrowser.sites import site

admin.autodiscover()

# administration password reset urls
urlpatterns = patterns('',
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='admin_password_reset'),
    url(r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)

# administration apps
urlpatterns += patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin', include(admin.site.urls)),
)

# Sitemaps
sitemaps = {
    'flatpages': FlatPageSitemap,
    'static': StaticViewSitemap,
    'posts': PostSitemap,
    'letters': LetterSitemap,
    'events': EventSitemap,
}
urlpatterns += patterns('',
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)

# tinyMCE editor
urlpatterns += patterns('',
    url(r'^tinymce/', include('tinymce.urls')),
)

# static files url patterns
urlpatterns += staticfiles_urlpatterns()

# serve static files from media directory when in debug mode
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
        url(r'^__debug__/', include(debug_toolbar.urls)),
   )

urlpatterns += patterns('',
    (r'^page/', include('django.contrib.flatpages.urls')),
)

# app urls
urlpatterns += patterns('',
    url(r'^letters/', include('letters.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^', include('events.urls')),
)
