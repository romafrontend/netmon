# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netobjects', '0002_blueprintnetworkobject_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blueprintnetworkobject',
            name='manufacturer',
        ),
        migrations.AddField(
            model_name='blueprintnetworkobject',
            name='model_family',
            field=models.CharField(max_length=20, null=True, verbose_name='Family'),
        ),
    ]
