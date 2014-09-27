# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date_of_event',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='event',
            name='color',
            field=models.CharField(default=b'#000000', max_length=22),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='do_color_inverse',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='do_get_guests',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='do_show_guests',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='do_show_proposals',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.date(2014, 9, 26)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guest',
            name='affiliation',
            field=models.CharField(max_length=160, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guest',
            name='proposal',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='guest',
            unique_together=set([('person', 'event')]),
        ),
    ]
