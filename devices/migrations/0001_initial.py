# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 07:02
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=100)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('diameter', models.IntegerField()),
                ('height', models.IntegerField()),
                ('water_level', models.IntegerField(blank=True, default=0)),
                ('type', django.contrib.postgres.fields.jsonb.JSONField(default={'class': 'source', 'location': 'overground'})),
            ],
            options={
                'verbose_name_plural': 'Tanks',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='pump',
            name='devices',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assoc_pump', to='devices.Tank'),
        ),
    ]
