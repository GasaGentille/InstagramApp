# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-21 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_image_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='User', max_length=30),
        ),
    ]
