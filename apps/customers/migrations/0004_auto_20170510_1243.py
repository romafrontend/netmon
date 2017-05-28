# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_company_ftp_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='ftp_username',
        ),
        migrations.AddField(
            model_name='company',
            name='ftp_login',
            field=models.CharField(blank=True, max_length=32, verbose_name='FTP Login'),
        ),
        migrations.AlterField(
            model_name='company',
            name='ftp_password',
            field=models.CharField(blank=True, max_length=64, verbose_name='FTP Password'),
        ),
    ]
