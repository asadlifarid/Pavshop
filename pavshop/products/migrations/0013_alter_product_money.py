# Generated by Django 4.1.7 on 2023-07-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_tag_products_product_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='money',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
