# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-15 07:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0013_auto_20180914_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images_links',
            old_name='image_id',
            new_name='img_id',
        ),
        migrations.RenameField(
            model_name='news_links',
            old_name='news_id',
            new_name='new_id',
        ),
        migrations.RenameField(
            model_name='youtube_links',
            old_name='video_id',
            new_name='vid_id',
        ),
    ]
