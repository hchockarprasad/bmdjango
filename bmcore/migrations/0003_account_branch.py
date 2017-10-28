# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 04:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bmcore', '0002_accountgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('alias_name', models.CharField(blank=True, max_length=55, null=True)),
                ('print_name', models.CharField(blank=True, max_length=55, null=True)),
                ('val_name', models.CharField(blank=True, max_length=55, null=True)),
                ('bwd', models.BooleanField()),
                ('door', models.CharField(blank=True, max_length=10, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('station', models.CharField(blank=True, max_length=20, null=True)),
                ('district', models.CharField(blank=True, max_length=15, null=True)),
                ('state', models.CharField(blank=True, max_length=15, null=True)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('fax', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('it_pan', models.CharField(blank=True, max_length=15, null=True)),
                ('gst_no', models.CharField(blank=True, max_length=15, null=True)),
                ('cst_no', models.CharField(blank=True, max_length=15, null=True)),
                ('tin_no', models.CharField(blank=True, max_length=15, null=True)),
                ('is_default', models.BooleanField(default=False)),
                ('default_name', models.CharField(blank=True, max_length=55, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_group', to='bmcore.AccountGroup')),
            ],
            options={
                'db_table': 'tbl_acc',
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('val_name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_default', models.BooleanField(default=False)),
                ('branch_type', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_branch',
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]
