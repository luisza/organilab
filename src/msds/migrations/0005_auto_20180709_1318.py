# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-09 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msds', '0004_organilabnode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organilabnode',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
