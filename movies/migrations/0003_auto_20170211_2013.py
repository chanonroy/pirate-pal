# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20170211_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(default='23jkldf', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='dvd_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
