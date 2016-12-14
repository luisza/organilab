# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0004_auto_20160826_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelf',
            name='type',
            field=models.CharField(choices=[('C', 'Space'), ('D', 'Drawer')], max_length=2, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='shelfobject',
            name='measurement_unit',
            field=models.CharField(choices=[('0', 'Meters'), ('1', 'Milimeters'), ('2', 'Centimeters'), ('3', 'Liters'), ('4', 'Mililiters'), ('5', 'Unit')], max_length=2, verbose_name='Measurement unit'),
        ),
    ]
