# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netobjects', '0003_auto_20170421_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blueprintnetworkobject',
            name='model_family',
            field=models.CharField(max_length=20, verbose_name='Family'),
        ),
    ]