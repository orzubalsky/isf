# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=140)),
                ('content', tinymce.models.HTMLField(null=True, blank=True)),
                ('slug', models.SlugField(max_length=160)),
                ('documents', models.ManyToManyField(to='base.Document', null=True, blank=True)),
                ('images', models.ManyToManyField(to='base.Image', null=True, blank=True)),
                ('sounds', models.ManyToManyField(to='base.Sound', null=True, blank=True)),
                ('videos', models.ManyToManyField(to='base.Video', null=True, blank=True)),
                ('vimeos', models.ManyToManyField(to='base.Vimeo', null=True, blank=True)),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
    ]
