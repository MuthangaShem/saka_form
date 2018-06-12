# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-12 06:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=60)),
                ('category_description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=60)),
                ('event_image', models.ImageField(null=True, upload_to='event-images/')),
                ('event_description', models.TextField()),
                ('event_location', models.CharField(max_length=60)),
                ('number_of_tickets', models.IntegerField()),
                ('event_type', models.CharField(max_length=60)),
                ('event_topic', models.CharField(max_length=255)),
                ('event_date', models.DateTimeField()),
                ('event_created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(max_length=80)),
                ('profile_email', models.CharField(max_length=100)),
                ('profile_interest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interests', to='app.Category')),
                ('profile_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
    ]
