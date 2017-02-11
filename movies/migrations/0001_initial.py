# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('photo', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('dvd_date', models.DateField(blank=True)),
            ],
        ),
    ]