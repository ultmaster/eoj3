# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0005_auto_20180809_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailrecipient',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emailrecipient',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]