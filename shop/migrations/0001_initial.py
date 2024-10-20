# Generated by Django 5.1.2 on 2024-10-20 11:08

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('hex_code', models.CharField(max_length=7, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SizeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_featured', models.BooleanField(default=False)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('additional_information', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='products/images/')),
                ('additional_image_1', models.ImageField(blank=True, null=True, upload_to='products/images/')),
                ('additional_image_2', models.ImageField(blank=True, null=True, upload_to='products/images/')),
                ('additional_image_3', models.ImageField(blank=True, null=True, upload_to='products/images/')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='products/videos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('branding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.branding')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category')),
                ('colors', models.ManyToManyField(related_name='products', to='shop.color')),
                ('size', models.ManyToManyField(related_name='products', to='shop.sizecategory')),
                ('tags', models.ManyToManyField(related_name='products', to='shop.tag')),
            ],
        ),
    ]
