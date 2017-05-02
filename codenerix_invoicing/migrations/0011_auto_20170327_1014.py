# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 10:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_invoicing', '0010_auto_20170327_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesbasket',
            name='rol',
            field=models.CharField(choices=[(b'SC', 'Shopping cart'), (b'BU', 'Budget'), (b'WL', 'Wish list')], default=b'SC', max_length=2, verbose_name='Rol basket'),
        ),
        migrations.AlterField(
            model_name='saleslinebasket',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_basket_sales', to='codenerix_invoicing.SalesBasket', verbose_name='Basket'),
        ),
    ]
