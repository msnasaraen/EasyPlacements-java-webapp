# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-11-22 03:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userModule', '0010_remove_admindetails_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=10)),
                ('rollno', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('birthday', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
                ('contact', models.BigIntegerField()),
                ('profilepicture', models.FileField(blank=True, null=True, upload_to=b'')),
                ('resume', models.FileField(blank=True, null=True, upload_to=b'')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]