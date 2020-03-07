# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-29 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('entered_by', models.CharField(max_length=40)),
                ('subj', models.CharField(max_length=80)),
                ('desc', models.TextField()),
                ('status', models.PositiveSmallIntegerField(default=1)),
                ('upvotes', models.PositiveIntegerField(default=0)),
                ('date_closed', models.DateField(blank=True, default=None, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
