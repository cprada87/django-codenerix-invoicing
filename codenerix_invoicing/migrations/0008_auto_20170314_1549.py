# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_products', '0004_auto_20170307_1045'),
        ('codenerix_payments', '0018_auto_20170303_0839'),
        ('codenerix_invoicing', '0007_auto_20170309_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('lock', models.BooleanField(default=False, verbose_name='Lock')),
                ('parent_pk', models.IntegerField(blank=True, null=True, verbose_name='Parent pk')),
                ('code', models.CharField(max_length=64, verbose_name='Code')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('observations', models.TextField(blank=True, max_length=256, null=True, verbose_name='Observations')),
                ('rol', models.CharField(choices=[((b'SC',), 'Shopping cart'), (b'BU', 'Budget'), (b'WL', 'Wish list')], default=(b'SC',), max_length=2, verbose_name='Rol basket')),
                ('signed', models.BooleanField(default=False, verbose_name='Signed')),
                ('public', models.BooleanField(default=False, verbose_name='Public')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_sales', to='codenerix_invoicing.Customer', verbose_name='Customer')),
                ('payment', models.ManyToManyField(blank=True, related_name='basket_sales', to='codenerix_payments.PaymentRequest', verbose_name='Payment Request')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalesLineBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('quantity', models.FloatField(verbose_name='Quantity')),
                ('notes', models.CharField(blank=True, max_length=256, null=True, verbose_name='Notes')),
                ('price_recommended', models.FloatField(verbose_name='Recomended price')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('discount', models.FloatField(default=0, verbose_name='Discount')),
                ('price', models.FloatField(verbose_name='Price')),
                ('tax', models.FloatField(blank=True, default=0, null=True, verbose_name='Tax')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_basket_sales', to='codenerix_invoicing.Customer', verbose_name='Basket')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_basket_sales', to='codenerix_products.ProductFinal', verbose_name='Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='salesbasket',
            unique_together=set([('code', 'parent_pk')]),
        ),
    ]
