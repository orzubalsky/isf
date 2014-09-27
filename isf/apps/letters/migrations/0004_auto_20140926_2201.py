# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20140926_2201'),
        ('letters', '0003_auto_20140926_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='related_events',
            field=models.ManyToManyField(to='events.Event', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='letter',
            name='related_letters',
            field=models.ManyToManyField(related_name='related_letters_rel_+', null=True, to='letters.Letter', blank=True),
            preserve_default=True,
        ),
    ]
