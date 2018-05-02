# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-02 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0029_contest_analysis_blog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='scoring_method',
            field=models.CharField(choices=[('acm', 'ACM Rule'), ('oi', 'OI Rule'), ('cf', 'School of Data Analysis (SDA) Rule'), ('tcmtime', 'TCM/TIME Rule')], default='acm', max_length=5),
        ),
    ]
