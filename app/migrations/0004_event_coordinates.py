# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-25 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180624_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='coordinates',
            field=models.DecimalField(decimal_places=10, max_digits=19, null=True),
        ),
    ]