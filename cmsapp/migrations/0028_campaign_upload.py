# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-22 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0027_campaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
