# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20140926_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='facebook_attending',
        ),
    ]
