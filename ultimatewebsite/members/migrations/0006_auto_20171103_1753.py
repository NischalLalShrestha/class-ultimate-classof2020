# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20171018_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='favourite_quote',
            field=models.CharField(blank=True, max_length=600),
        ),
    ]
