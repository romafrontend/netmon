# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-15 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firewalls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ipv4_address', models.CharField(max_length=16)),
                ('login', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('site_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
