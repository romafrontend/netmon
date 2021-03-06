# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netobjects', '0004_auto_20170421_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blueprintnetworkobject',
            name='object_type',
            field=models.CharField(choices=[('FI', 'Firewall'), ('RO', 'Router'), ('SW', 'Switch'), ('AC', 'Access Point'), ('IP', 'IPPBX')], max_length=2),
        ),
        migrations.AlterField(
            model_name='firewall',
            name='web_address',
            field=models.CharField(default='https://', max_length=100),
        ),
        migrations.AlterField(
            model_name='router',
            name='web_address',
            field=models.CharField(default='https://', max_length=100),
        ),
    ]
