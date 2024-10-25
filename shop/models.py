import random

from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.db import models
from django.db.models.signals import pre_save


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    is_visible = models.BooleanField(default=True)

    def __iter__(self):
        products = self.products.filter(is_visible=True).order_by('name')
        for product in products:
            yield product

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Branding(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=100, unique=True)
    is_visible = models.BooleanField(default=True)

    def __iter__(self):
        products = self.products.filter(is_visible=True).order_by('name')
        for product in products:
            yield product

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SizeCategory(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=100, unique=True)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __iter__(self):
        products = self.products.filter(is_visible=True).order_by('size')
        for product in products:
            yield product

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    hex_code = ColorField(default='#FF0000', unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __iter__(self):
        products = self.products.filter(is_visible=True).order_by('color')
        for product in products:
            yield product

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.hex_code
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True)
    is_visible = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __iter__(self):
        products = self.products.filter(is_visible=True).order_by('color')
        for product in products:
            yield product

    def __str__(self):
        return self.name

class Product(models.Model):
    CURRENCY_CHOICES = [
        ('$', 'USD'),
        ('€', 'EUR'),
        ('UAH', 'UAH'),
    ]

    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=100, unique=True)
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')
    branding = models.ForeignKey(Branding, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    is_featured = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    note = RichTextField(blank=True, null=True)
    size = models.ManyToManyField(SizeCategory, related_name='products')
    colors = models.ManyToManyField(Color, related_name='products')
    tags = models.ManyToManyField(Tag, related_name='products')
    quantity = models.PositiveIntegerField(default=0)
    is_liked = models.BooleanField(default=False)
    description = RichTextField(blank=True, null=True)
    additional_information = RichTextField(blank=True, null=True)

    main_image = models.ImageField(upload_to='products/images/', blank=True, null=True)
    additional_image_1 = models.ImageField(upload_to='products/images/', blank=True, null=True)
    additional_image_2 = models.ImageField(upload_to='products/images/', blank=True, null=True)
    additional_image_3 = models.ImageField(upload_to='products/images/', blank=True, null=True)

    video_file = models.FileField(upload_to='products/videos/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
