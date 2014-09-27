from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from base.admin import *
from letters.models import *
from letters.resources import SignatureResource


class SignatureAdmin(ImportExportModelAdmin):
    resource_class = SignatureResource
    pass


admin.site.register(Letter)
admin.site.register(Signature, SignatureAdmin)
