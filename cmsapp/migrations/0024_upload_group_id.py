# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-25 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0023_auto_20181024_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='group_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]