# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0002_auto_20140925_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='color',
            field=models.CharField(default=b'#000000', max_length=22),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='letter',
            name='do_color_inverse',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='letter',
            name='do_get_signatures',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='letter',
            name='do_show_signatures',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
