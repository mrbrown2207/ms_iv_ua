# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-18 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature', '0002_auto_20200216_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='status',
            field=models.PositiveSmallIntegerField(default=5),
        ),
    ]