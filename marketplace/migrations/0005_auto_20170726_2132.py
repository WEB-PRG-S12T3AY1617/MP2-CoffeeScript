# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 13:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_auto_20170726_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='type',
            new_name='degree_OR_office',
        ),
    ]
