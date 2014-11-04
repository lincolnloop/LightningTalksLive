# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import LTL.core.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('presenters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', LTL.core.models.CreationDateTimeField(default=django.utils.timezone.now, verbose_name=b'created', editable=False, blank=True)),
                ('modified', LTL.core.models.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name=b'modified', editable=False, blank=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('when', models.DateTimeField()),
                ('topics', models.CharField(max_length=255, null=True, blank=True)),
                ('presenter', models.ForeignKey(to='presenters.Profile')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
    ]
