# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backups', '0007_auto_20170503_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corebackup',
            name='ftp_user_login',
        ),
        migrations.RemoveField(
            model_name='corebackup',
            name='ftp_user_password',
        ),
    ]