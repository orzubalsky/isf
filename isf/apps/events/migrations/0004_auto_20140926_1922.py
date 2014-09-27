# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20140926_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
