# Generated by Django 2.2.dev20180611123309 on 2018-07-02 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='gmtime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='entry',
            name='hashed_hostname',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='entry',
            name='login',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='entry',
            name='action',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='entry',
            name='cdat_info_version',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='entry',
            name='domain',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='entry',
            name='pid',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='entry',
            name='platform',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='entry',
            name='platform_version',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='entry',
            name='sleep',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='entry',
            name='source',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='entry',
            name='source_version',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]
