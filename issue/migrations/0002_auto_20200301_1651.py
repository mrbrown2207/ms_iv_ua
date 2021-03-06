# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-01 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='entered_by_email',
            field=models.EmailField(blank=True, default=None, max_length=80),
        ),
        migrations.AlterField(
            model_name='issue',
            name='entered_by',
            field=models.CharField(blank=True, default=None, max_length=40),
        ),
    ]
