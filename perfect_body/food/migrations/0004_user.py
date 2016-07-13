# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20160315_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(default=123, max_length=20)),
                ('gender', models.CharField(max_length=1)),
                ('years', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('BMI', models.FloatField(default=0)),
            ],
        ),
    ]