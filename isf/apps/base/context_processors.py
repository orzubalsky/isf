from django.conf import settings


def google_analytics(request):
    if settings.GOOGLE_ANALYTICS_KEY:
        return {'GOOGLE_ANALYTICS_KEY': settings.GOOGLE_ANALYTICS_KEY}
