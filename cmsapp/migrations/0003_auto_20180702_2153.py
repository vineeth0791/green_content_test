# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-02 21:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0002_image_links'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image_links',
            new_name='Images_links',
        ),
    ]
