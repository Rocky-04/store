# Generated by Django 4.1.1 on 2022-10-25 09:00

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100,
                                           verbose_name='Категория')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('photo',
                 models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('category',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.PROTECT,
                                   to='news.category')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'ordering': ['-created_at', 'title'],
            },
        ),
    ]
