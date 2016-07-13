# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('weight', models.FloatField()),
                ('quantity', models.FloatField()),
                ('calories', models.IntegerField()),
            ],
        ),
    ]