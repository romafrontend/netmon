# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
