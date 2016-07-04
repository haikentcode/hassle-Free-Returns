# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 13:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Condition',
            new_name='Order',
        ),
        migrations.RemoveField(
            model_name='category',
            name='typelist',
        ),
        migrations.RemoveField(
            model_name='categorytypes',
            name='physicalCondition',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='orderid',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='CategoryTypes',
        ),
    ]
