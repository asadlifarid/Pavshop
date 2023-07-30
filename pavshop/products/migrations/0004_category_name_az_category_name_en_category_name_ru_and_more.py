# Generated by Django 4.1.7 on 2023-06-27 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_brand_slug_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_az',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='small_description_az',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='small_description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='small_description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_az',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='name_az',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
