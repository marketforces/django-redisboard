# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-09-14 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redisboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='redisserver',
            name='keys_filter',
            field=models.CharField(default='*', help_text='Parameter to pass the KEYS command for the list of keys to show. Defaults to all keys.', max_length=50, verbose_name='Key filter'),
        ),
    ]
