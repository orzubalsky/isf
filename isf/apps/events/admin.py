from django.contrib import admin
from base.admin import *
from events.models import *

admin.site.register(Event)
admin.site.register(Guest)
