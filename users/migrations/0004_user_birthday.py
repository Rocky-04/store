# Generated by Django 4.1.1 on 2022-10-17 06:04

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0003_remove_user_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, default=None, null=True,
                                   verbose_name='Дата народження'),
        ),
    ]
