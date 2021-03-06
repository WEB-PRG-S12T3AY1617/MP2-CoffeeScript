# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_user_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='occupation',
            field=models.CharField(choices=[('student', 'Student'), ('staff', 'Staff')], default='student', max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
