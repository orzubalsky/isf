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
            name='Letter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=160)),
                ('body', tinymce.models.HTMLField()),
                ('date_published', models.DateTimeField()),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('letter', models.ForeignKey(to='letters.Letter')),
                ('person', models.ForeignKey(to='base.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='letter',
            name='signatures',
            field=models.ManyToManyField(to='base.Person', null=True, through='letters.Signature', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='letter',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
