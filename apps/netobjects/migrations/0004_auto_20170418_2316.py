# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netobjects', '0003_auto_20170418_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firewall',
            name='cli_address',
            field=models.CharField(blank=True, editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='router',
            name='cli_address',
            field=models.CharField(blank=True, editable=False, max_length=255),
        ),
    ]
