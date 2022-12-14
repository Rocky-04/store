# Generated by Django 4.1.3 on 2022-11-16 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_product_counnt_reviews_product_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='counnt_reviews',
            new_name='count_reviews',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='vendorCode',
            new_name='vendor_code',
        ),
        migrations.AlterField(
            model_name='reviews',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='shop.product'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Normal'), (4, 'OK'), (5, 'Very good')]),
        ),
    ]
