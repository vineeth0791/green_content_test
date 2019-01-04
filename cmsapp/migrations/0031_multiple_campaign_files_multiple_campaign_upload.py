# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-28 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0030_single_campaign_upload_campaign_uploaded_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multiple_campaign_files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Multiple_campaign', models.CharField(max_length=10)),
                ('mul_files', models.FileField(upload_to='campaigns/multiple_region')),
            ],
        ),
        migrations.CreateModel(
            name='Multiple_campaign_upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_uploaded_by', models.CharField(max_length=10)),
                ('campaign_name', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField()),
                ('updated_date', models.DateTimeField()),
            ],
        ),
    ]