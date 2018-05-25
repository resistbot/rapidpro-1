# Generated by Django 1.11.6 on 2018-01-26 14:52

import django.contrib.postgres.fields
from django.db import migrations, models
import temba.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('msgs', '0113_auto_20171128_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcast',
            name='media',
            field=temba.utils.models.TranslatableField(help_text='The localized versions of the media', max_length=2048, null=True, verbose_name='Media'),
        ),
        migrations.AlterField(
            model_name='msg',
            name='attachments',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=2048), help_text='The media attachments on this message if any', null=True, size=None),
        ),
    ]
