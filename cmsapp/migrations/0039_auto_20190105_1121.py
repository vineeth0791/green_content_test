# Generated by Django 2.0.9 on 2019-01-05 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0038_upload_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='upload',
            field=models.FileField(upload_to=''),
        ),
    ]