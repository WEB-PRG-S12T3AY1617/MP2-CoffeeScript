# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 13:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_auto_20170815_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
