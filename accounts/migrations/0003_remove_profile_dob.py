# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-02 06:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_foo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='dob',
        ),
    ]