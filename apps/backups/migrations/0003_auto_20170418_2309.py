# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backups', '0002_auto_20170418_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backupfirewall',
            name='site_name',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='backuprouter',
            name='site_name',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
