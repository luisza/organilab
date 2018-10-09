# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-23 02:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sga', '0006_auto_20180822_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrudenceAdvice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Name')),
            ],
        ),
        migrations.DeleteModel(
            name='prudence_advice',
        ),
        migrations.RemoveField(
            model_name='dangerindication',
            name='prudence_advice',
        ),
        migrations.AlterField(
            model_name='dangerindication',
            name='warning_words',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sga.WarningWord', verbose_name='Warning words'),
        ),
        migrations.AddField(
            model_name='dangerindication',
            name='prudence_advice',
            field=models.ManyToManyField(to='sga.PrudenceAdvice', verbose_name='Prudence advice'),
        ),
    ]