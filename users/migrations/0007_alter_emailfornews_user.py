# Generated by Django 4.1.1 on 2022-10-21 08:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0006_emailfornews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailfornews',
            name='user',
            field=models.OneToOneField(blank=True, null=True,
                                       on_delete=django.db.models.deletion.CASCADE,
                                       related_name='email_for_news',
                                       to=settings.AUTH_USER_MODEL),
        ),
    ]