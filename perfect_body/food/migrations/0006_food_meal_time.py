# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20160316_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='meal_time',
            field=models.CharField(default='breakfast', max_length=20),
            preserve_default=False,
        ),
    ]
