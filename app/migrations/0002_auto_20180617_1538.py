# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-17 12:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_charges',
            field=models.CharField(max_length=8, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid amount', regex='^(\\d{1,5})$')]),
        ),
        migrations.AddField(
            model_name='event',
            name='event_status',
            field=models.CharField(choices=[('F', 'FREE'), ('P', 'PAID')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='number_of_tickets',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Enter a valid number', regex='^(\\d{1,5})$')]),
        ),
    ]