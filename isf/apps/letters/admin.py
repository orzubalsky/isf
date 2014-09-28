from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from base.admin import *
from letters.models import *
from letters.resources import SignatureResource


class SignatureInline(admin.TabularInline):
    """
    """
    model = Signature
    fields = (
        'person',
        'comment',
        'is_active'
    )
    extra = 0


class SignatureAdmin(ImportExportModelAdmin):
    resource_class = SignatureResource
    fields = (
        'person',
        'letter',
        'comment',
    )
    list_display = (
        'person',
        'letter',
        'created',
        'is_active'
    )


class LetterAdmin(BaseAdmin):
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        ]

    fieldsets = (
        ('Info', {
            'fields': (
                'title',
                'slug',
                'body',
                'is_active'
            )
        }),
        ('Settings', {
            'fields': (
                'color',
                'do_color_inverse',
                'do_get_signatures',
                'do_show_signatures',
                'related_events',
                'related_letters',
                'tags'
            )
        }),
    )
    list_display = (
        'title',
        'color',
        'do_color_inverse',
        'do_get_signatures',
        'do_show_signatures',
        'is_active'
    )
    list_editable = (
        'color',
        'do_color_inverse',
        'do_get_signatures',
        'do_show_signatures',
        'is_active',
    )
    prepopulated_fields = {'slug': ('title',)}
    # inlines = (SignatureInline, )


admin.site.register(Letter, LetterAdmin)
admin.site.register(Signature, SignatureAdmin)
