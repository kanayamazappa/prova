# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20160224_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='G\xeanero'),
        ),
    ]
