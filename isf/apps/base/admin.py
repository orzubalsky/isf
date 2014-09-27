from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from base.resources import PersonResource
from base.models import Person


class BaseAdmin(admin.ModelAdmin):
    """
    """
    pass


class PersonAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = PersonResource
    pass


# register admin models
admin.site.register(Person, PersonAdmin)
# admin.site.register(Video)
# admin.site.register(Vimeo)
