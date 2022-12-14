# Generated by Django 4.1.1 on 2022-10-18 05:27

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('shop',
         '0003_tag_description_en_tag_description_uk_tag_title_en_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category',
                     'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['title'], 'verbose_name': 'Country',
                     'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['title'], 'verbose_name': 'Tag',
                     'verbose_name_plural': 'Tags'},
        ),
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, null=True,
                                    upload_to='photo/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0,
                                      max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description_en',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description_uk',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='picture',
            field=models.ImageField(blank=True, null=True,
                                    upload_to='photo/%Y/%m/%d/',
                                    verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title_en',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title_two',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title_two_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title_two_uk',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title_uk',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
