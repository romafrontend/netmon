# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('netobjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blueprintnetworkobject',
            name='company_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.Company'),
        ),
    ]
