# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-17 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0002_auto_20180515_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archive',
            old_name='archive_hash',
            new_name='hash',
        ),
        migrations.RenameField(
            model_name='archive',
            old_name='archive_url',
            new_name='url',
        ),
        migrations.RemoveField(
            model_name='archive',
            name='archive_size',
        ),
        migrations.RemoveField(
            model_name='archive',
            name='end_date',
        ),
        migrations.AddField(
            model_name='archive',
            name='period',
            field=models.CharField(choices=[('D', 'Day'), ('M', 'Month')], default='D', help_text='The length of time this archive covers', max_length=1),
        ),
        migrations.AddField(
            model_name='archive',
            name='rollup',
            field=models.ForeignKey(help_text='The archive we were rolled up into, if any', null=True, on_delete=django.db.models.deletion.SET_NULL, to='archives.Archive'),
        ),
        migrations.AddField(
            model_name='archive',
            name='size',
            field=models.BigIntegerField(default=0, help_text='The size of this archive in bytes (after gzipping)'),
        ),
    ]
