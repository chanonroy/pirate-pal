# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20170211_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='photo',
            field=models.CharField(max_length=250),
        ),
    ]
