# Generated by Django 4.1.1 on 2022-10-16 12:41

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('session_key',
                 models.CharField(blank=True, default=None, max_length=128,
                                  null=True)),
                ('nmb', models.IntegerField(default=1)),
                ('price_per_item',
                 models.DecimalField(decimal_places=0, default=0,
                                     max_digits=10)),
                ('total_price',
                 models.DecimalField(decimal_places=0, default=0,
                                     max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('color',
                 models.ForeignKey(blank=True, default=None, null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='shop.attributecolor')),
                ('product',
                 models.ForeignKey(blank=True, default=None, null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='shop.product')),
                ('size',
                 models.ForeignKey(blank=True, default=None, null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='shop.attributesize')),
            ],
            options={
                'verbose_name': 'Товари в корзині',
                'verbose_name_plural': 'Товари в корзині',
            },
        ),
    ]
