# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20140926_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='affiliation',
            field=models.CharField(help_text=b'Are you in a group or organization that you think will interest others? (optional)', max_length=160, null=True, verbose_name=b'Group or organization', blank=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='proposal',
            field=models.TextField(help_text=b'What would you like to talk about or work on in this event? (optional)', null=True, blank=True),
        ),
    ]
