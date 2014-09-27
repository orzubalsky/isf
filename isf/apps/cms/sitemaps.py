from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from django.contrib.sitemaps import ping_google
from cms.models import *


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'info', 'post-list']

    def location(self, item):
        return reverse(item)

    def save(self, force_insert=False, force_update=False):
        super(StaticViewSitemap, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass


class PostSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def save(self, force_insert=False, force_update=False):
        super(PostSitemap, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass

    def items(self):
        return Post.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated

    def location(self, item):
        return reverse('post-detail', kwargs={'slug': item.slug})
