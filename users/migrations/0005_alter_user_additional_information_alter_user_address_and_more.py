# Generated by Django 4.1.1 on 2022-10-18 06:08

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0004_user_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='additional_information',
            field=models.CharField(blank=True, default=None, max_length=300,
                                   null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=200,
                                   null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=200,
                                   null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, default=None, max_length=200,
                                   null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='postcode',
            field=models.CharField(blank=True, default=None, max_length=200,
                                   null=True),
        ),
    ]
