# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0002_auto_20170328_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='control',
            field=models.CharField(max_length=128),
        ),
    ]
