# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-11 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0017_my_gc_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_gc_group',
            name='tagged_email',
        ),
        migrations.AddField(
            model_name='my_gc_group',
            name='tagged_emails',
            field=models.TextField(blank=True, null=True),
        ),
    ]
