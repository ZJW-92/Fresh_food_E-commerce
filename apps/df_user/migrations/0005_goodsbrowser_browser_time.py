# Generated by Django 2.0.3 on 2022-03-27 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0004_auto_20181218_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsbrowser',
            name='browser_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='browse time'),
        ),
    ]
