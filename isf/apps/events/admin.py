from django.contrib import admin
from base.admin import *
from events.models import *


class GuestInline(admin.TabularInline):
    """
    """
    model = Guest
    fields = (
        'person',
        'affiliation',
        'proposal',
        'comment',
        'is_public',
        'attending_status'
    )
    extra = 0


class GuestAdmin(BaseAdmin):
    fields = (
        'person',
        'event',
        'affiliation',
        'proposal',
        'comment',
        'is_public',
        'attending_status'
    )
    list_display = (
        'person',
        'event',
        'affiliation',
        'attending_status',
        'created',
        'is_active'
    )


class EventAdmin(BaseAdmin):
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        ]

    fieldsets = (
        ('Info', {
            'fields': (
                'title',
                'slug',
                'start_date',
                'end_date',
                'hosted_by',
                'description',
                'is_active'
            )
        }),
        ('Address', {
            'fields': (
                'street_address',
                'city',
                'state',
                'zip_code',
                'telephone',
                'latitude',
                'longitude'
            )
        }),
        ('Settings', {
            'fields': (
                'color',
                'do_color_inverse',
                'do_get_guests',
                'do_show_guests',
                'do_show_proposals',
                'facebook_id',
                'related_events',
                'related_letters',
                'tags'
            )
        }),
    )
    list_display = (
        'title',
        'start_date',
        'end_date',
        'color',
        'do_color_inverse',
        'do_get_guests',
        'do_show_guests',
        'do_show_proposals',
        'is_active'
    )
    list_editable = (
        'color',
        'do_color_inverse',
        'do_get_guests',
        'do_show_guests',
        'do_show_proposals',
        'is_active',
    )
    prepopulated_fields = {'slug': ('title',)}
    inlines = (GuestInline, )


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
