# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 11:34
from __future__ import unicode_literals

import codenerix.fields
import codenerix.lib.helpers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_invoicing', '0015_auto_20170405_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Haulier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('image', codenerix.fields.ImageAngularField(blank=True, max_length=200, null=True, upload_to=codenerix.lib.helpers.upload_path, verbose_name='Image')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('url_public', models.CharField(blank=True, max_length=250, null=True, verbose_name='Url public')),
                ('url_tracking', models.CharField(blank=True, max_length=250, null=True, verbose_name='Url tracking')),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='salesorder',
            name='number_tracking',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Number of tracking'),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='haulier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_sales', to='codenerix_invoicing.Haulier', verbose_name='Haulier'),
        ),
    ]
