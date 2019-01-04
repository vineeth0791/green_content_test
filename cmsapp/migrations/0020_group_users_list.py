# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-11 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0019_auto_20181011_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group_users_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_emails_list', models.TextField()),
                ('saved_emails_date', models.DateTimeField()),
                ('gc_groups', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsapp.My_GC_Groups')),
            ],
        ),
    ]