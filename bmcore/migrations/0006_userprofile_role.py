# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bmcore', '0005_auto_20171028_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bmcore.Role'),
        ),
    ]
