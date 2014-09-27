from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from django.contrib.sitemaps import ping_google
from events.models import *


class EventSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def save(self, force_insert=False, force_update=False):
        super(EventSitemap, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass

    def items(self):
        return Event.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated

    def location(self, item):
        return reverse('event-detail', kwargs={'slug': item.slug})
