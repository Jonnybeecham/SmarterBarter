# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerID', models.CharField(default='5555555', max_length=7)),
                ('firstName', models.CharField(default='first', max_length=200)),
                ('lastName', models.CharField(default='last', max_length=200)),
                ('userName', models.CharField(default='user', max_length=200)),
                ('zipCode', models.IntegerField(default='55555')),
                ('email', models.EmailField(max_length=500)),
                ('password', models.CharField(default='password', max_length=20)),
                ('bio', models.TextField(default='Text Here', max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicesID', models.CharField(max_length=60)),
                ('needsID', models.CharField(max_length=60)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Customer')),
            ],
        ),
    ]
