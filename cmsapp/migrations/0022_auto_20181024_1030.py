# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-24 10:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0021_auto_20181011_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keys', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='upload',
            name='keys',
        ),
        migrations.AddField(
            model_name='keywords',
            name='uploaded',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsapp.Upload'),
        ),
    ]