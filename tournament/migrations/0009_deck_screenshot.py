# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0008_auto_20170426_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='screens/'),
        ),
    ]
