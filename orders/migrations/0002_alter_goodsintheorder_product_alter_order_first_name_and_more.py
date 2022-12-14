# Generated by Django 4.1.1 on 2022-10-19 08:03

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0008_delete_status'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsintheorder',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to='shop.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(blank=True, max_length=200,
                                   verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=200),
        ),
    ]
