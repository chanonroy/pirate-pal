# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 20:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_auto_20170211_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
