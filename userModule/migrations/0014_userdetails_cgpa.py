# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-11-26 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userModule', '0013_userdetails_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='cgpa',
            field=models.FloatField(default=7),
            preserve_default=False,
        ),
    ]