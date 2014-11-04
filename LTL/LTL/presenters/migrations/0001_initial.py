# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import LTL.core.models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', LTL.core.models.CreationDateTimeField(default=django.utils.timezone.now, verbose_name=b'created', editable=False, blank=True)),
                ('modified', LTL.core.models.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name=b'modified', editable=False, blank=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('twitter', models.URLField(null=True, blank=True)),
                ('linked_in', models.URLField(null=True, blank=True)),
                ('avatar', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('company', models.URLField(null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
    ]
