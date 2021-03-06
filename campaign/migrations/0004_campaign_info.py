# Generated by Django 2.0.9 on 2019-01-28 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cmsapp', '0042_multiple_campaign_upload_stor_location'),
        ('campaign', '0003_delete_multiple_campaign_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='campaign_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
                ('campaign_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsapp.Multiple_campaign_upload')),
            ],
        ),
    ]
