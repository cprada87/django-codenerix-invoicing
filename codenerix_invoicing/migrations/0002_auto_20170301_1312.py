# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 13:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_invoicing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseslineorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_order_purchases', to='codenerix_invoicing.PurchasesOrder', verbose_name='Orden'),
        ),
        migrations.AlterField(
            model_name='purchasesorderdocument',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderdocument_purchases', to='codenerix_invoicing.PurchasesOrder', verbose_name='Orden'),
        ),
        migrations.AlterField(
            model_name='saleslineorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_order_sales', to='codenerix_invoicing.SalesOrder', verbose_name='Orden'),
        ),
    ]
