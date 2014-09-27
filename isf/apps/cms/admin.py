from django.contrib import admin
from base.admin import *
from cms.models import *


class PostAdmin(BaseAdmin):
    """
    """
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        ]

    fieldsets = (
        ('Info', {
            'fields': (
                'name',
                'content',
                'slug',
                'source_link',
                'episodes',
                'created',
                'updated',
                'is_active'
            )
        }),
        ('Media', {
            'fields': ('images', 'sounds', 'videos', 'vimeos', 'documents')
        }),
    )
    list_display = ('name', 'created', 'updated', 'is_active')
    list_editable = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}


# register admin models
admin.site.register(Post, PostAdmin)
