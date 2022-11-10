# Generated by Django 4.1.1 on 2022-10-27 07:39

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_uk',
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='content_en',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='content_uk',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_uk',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True,
                                    on_delete=django.db.models.deletion.PROTECT,
                                    related_name='news', to='news.category'),
        ),
    ]