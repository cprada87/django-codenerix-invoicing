# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 12:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_invoicing', '0012_auto_20170405_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesbasket',
            old_name='rol',
            new_name='role',
        ),
    ]
