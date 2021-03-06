# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.URLField(max_length=256)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('event_type', models.CharField(max_length=64)),
                ('json_data', models.CharField(max_length=1024)),
            ],
        ),
    ]
