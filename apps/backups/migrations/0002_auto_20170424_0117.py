# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 22:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backupfirewall',
            name='file_location',
        ),
        migrations.RemoveField(
            model_name='backupfirewall',
            name='site_name',
        ),
        migrations.RemoveField(
            model_name='backuprouter',
            name='file_location',
        ),
        migrations.RemoveField(
            model_name='backuprouter',
            name='site_name',
        ),
    ]
