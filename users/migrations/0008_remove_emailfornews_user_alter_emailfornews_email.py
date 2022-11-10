# Generated by Django 4.1.1 on 2022-10-21 08:13

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0007_alter_emailfornews_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailfornews',
            name='user',
        ),
        migrations.AlterField(
            model_name='emailfornews',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
