from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from base.resources import PersonResource
from base.models import Person


class BaseAdmin(admin.ModelAdmin):
    """
    """
    pass


class PersonInline(admin.TabularInline):
    """
    """
    model = Person
    fields = (
        'name',
        'email',
        'is_active'
    )
    extra = 0


class PersonAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = PersonResource
    fields = ('name', 'email')
    list_display = ('name', 'email', 'created', 'is_active')
    list_editable = ('is_active', 'email')


# register admin models
admin.site.register(Person, PersonAdmin)
