# Generated by Django 2.2.dev20180611123309 on 2018-07-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usage', '0002_auto_20180702_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='login',
        ),
        migrations.AddField(
            model_name='entry',
            name='hashed_username',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]