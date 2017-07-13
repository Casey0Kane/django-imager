# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0006_merge_20170713_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageralbum',
            name='photo',
        ),
        migrations.AddField(
            model_name='imageralbum',
            name='photos',
            field=models.ManyToManyField(blank=True, default='', related_name='albums', to='imager_images.ImagerPhoto'),
        ),
    ]