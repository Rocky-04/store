# Generated by Django 4.1.1 on 2022-10-17 03:31

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='additional_information',
            field=models.CharField(blank=True, default=None, max_length=200,
                                   null=True,
                                   verbose_name='Додаткова інформація'),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=200,
                                   null=True, verbose_name='Адреса'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=200,
                                   null=True, verbose_name='Місто'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, default=None, max_length=200,
                                   null=True, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='user',
            name='postcode',
            field=models.CharField(blank=True, default=None, max_length=200,
                                   null=True, verbose_name='Індекс'),
        ),
    ]
