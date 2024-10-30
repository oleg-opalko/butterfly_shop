from django.db import models

from shop.models import Category


# Create your models here.

class BannerCollection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='banners/', blank=True, null=True)

    def __str__(self):
        return self.title


class ClothingBanner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)





