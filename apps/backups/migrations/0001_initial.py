# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('netobjects', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackupFirewall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('time_interval', models.IntegerField(default=1)),
                ('file_location', models.CharField(max_length=255)),
                ('object_backup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netobjects.Firewall')),
                ('site_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BackupRouter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('time_interval', models.IntegerField(default=1)),
                ('file_location', models.CharField(max_length=255)),
                ('object_backup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netobjects.Router')),
                ('site_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
