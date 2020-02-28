# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-28 11:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('org', models.CharField(blank=True, max_length=40)),
                ('org_web_site', models.URLField(blank=True)),
                ('title', models.CharField(blank=True, max_length=40)),
                ('dob', models.DateField(blank=True)),
            ],
        ),
    ]