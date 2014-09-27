# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0003_auto_20140926_1637'),
        ('events', '0006_remove_event_facebook_attending'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='related_events',
            field=models.ManyToManyField(related_name='related_events_rel_+', null=True, to='events.Event', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='related_letters',
            field=models.ManyToManyField(to='letters.Letter', null=True, blank=True),
            preserve_default=True,
        ),
    ]
