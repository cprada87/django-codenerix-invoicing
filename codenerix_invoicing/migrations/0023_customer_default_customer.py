# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-24 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_invoicing', '0022_auto_20170724_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='default_customer',
            field=models.BooleanField(default=False, verbose_name='Default customer'),
        ),
    ]
