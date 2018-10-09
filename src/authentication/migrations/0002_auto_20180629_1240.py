# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 18:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackentry',
            name='laboratory_id',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='feedbackentry',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='feedbackentry',
            name='explanation',
            field=models.TextField(blank=True, null=True, verbose_name='Explanation'),
        ),
        migrations.AlterField(
            model_name='feedbackentry',
            name='related_file',
            field=models.FileField(blank=True, null=True, upload_to='media/feedback_entries/', verbose_name='Related file'),
        ),
    ]
