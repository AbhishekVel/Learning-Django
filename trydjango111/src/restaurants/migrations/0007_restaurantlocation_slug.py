# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-18 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_auto_20180117_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]