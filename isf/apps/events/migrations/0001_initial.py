# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=160)),
                ('description', tinymce.models.HTMLField()),
                ('date_of_event', models.DateTimeField()),
                ('hosted_by', models.CharField(max_length=255, null=True, blank=True)),
                ('street_address', models.CharField(max_length=255, null=True, blank=True)),
                ('city', models.CharField(max_length=64, null=True, blank=True)),
                ('state', models.CharField(max_length=64, null=True, blank=True)),
                ('zip_code', models.CharField(max_length=10, null=True, blank=True)),
                ('telephone', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('is_public', models.BooleanField(default=False)),
                ('attending_status', models.CharField(default=b'no_rsvp', max_length=32, choices=[(b'yes', b'Yes'), (b'no', b'No'), (b'maybe', b'Maybe'), (b'no_rsvp', b"Hasn't RSVPed yet")])),
                ('event', models.ForeignKey(to='events.Event')),
                ('person', models.ForeignKey(to='base.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='guests',
            field=models.ManyToManyField(to='base.Person', null=True, through='events.Guest', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
