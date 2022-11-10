# Generated by Django 4.1.1 on 2022-10-18 05:44

import django.db.models.deletion
import mptt.fields
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0004_alter_category_options_alter_country_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attributecolor',
            options={'verbose_name': 'AttributeColor',
                     'verbose_name_plural': 'AttributeColors'},
        ),
        migrations.AlterModelOptions(
            name='attributecolorimage',
            options={'verbose_name': 'image', 'verbose_name_plural': 'images'},
        ),
        migrations.AlterModelOptions(
            name='attributesize',
            options={'verbose_name': 'AttributeSize',
                     'verbose_name_plural': 'AttributeSizes'},
        ),
        migrations.AlterModelOptions(
            name='banner',
            options={'ordering': ['pk'], 'verbose_name': 'Banner',
                     'verbose_name_plural': 'Banners'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': 'Color', 'verbose_name_plural': 'Colors'},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'ordering': ['title'], 'verbose_name': 'Currency',
                     'verbose_name_plural': 'Currencies'},
        ),
        migrations.AlterModelOptions(
            name='delivery',
            options={'ordering': ['price'], 'verbose_name': 'shipping cost',
                     'verbose_name_plural': 'cost of delivery'},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ['title'], 'verbose_name': 'brand',
                     'verbose_name_plural': 'brands'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-available', '-count_sale', '-created_at',
                                  'price'], 'verbose_name': 'Product',
                     'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'Size', 'verbose_name_plural': 'Sizes'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status',
                     'verbose_name_plural': 'Statuses'},
        ),
        migrations.AlterField(
            model_name='attributecolor',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='attributecolorimage',
            name='images',
            field=models.FileField(upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='attributesize',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='order_price',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='picture',
            field=models.ImageField(blank=True, null=True,
                                    upload_to='photo/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=mptt.fields.TreeForeignKey(null=True,
                                             on_delete=django.db.models.deletion.PROTECT,
                                             to='shop.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='count_sale',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='country',
            field=models.ForeignKey(blank=True, default=1, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to='shop.country'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.ForeignKey(default=1, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to='shop.currency'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=0, default=0,
                                      max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(blank=True, default=1, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='manufacturer',
                                    to='shop.manufacturer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='param',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendorCode',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
