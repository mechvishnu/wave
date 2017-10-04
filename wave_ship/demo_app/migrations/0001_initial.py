# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_name', models.CharField(max_length=50, unique=True)),
                ('port_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal_name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('email_ops', models.EmailField(max_length=254)),
                ('email_da', models.EmailField(max_length=254)),
                ('attention', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('state_province', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
                ('customer_ops_comments', models.CharField(max_length=50)),
                ('customer_da_comments', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('fax', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vessel_name', models.CharField(max_length=50, unique=True)),
                ('vessel_type', models.CharField(max_length=50)),
                ('nrt', models.CharField(max_length=50)),
                ('imo', models.CharField(max_length=50)),
                ('dwt', models.CharField(max_length=50)),
                ('grt', models.CharField(max_length=50)),
                ('loa', models.CharField(max_length=50)),
                ('registered', models.CharField(max_length=50)),
                ('displacement', models.CharField(max_length=50)),
                ('bow_thruster', models.CharField(max_length=50)),
            ],
        ),
    ]
