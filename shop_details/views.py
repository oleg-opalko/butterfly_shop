from django.shortcuts import render, get_object_or_404
from django.utils.lorem_ipsum import words

from shop.models import Product


# Create your views here.

def shop_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    images = [product.main_image, product.additional_image_1, product.additional_image_2, product.additional_image_3]

    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]

    context = {
        'product': product,
        'images': images,
        'related_products': related_products,
    }

    return render(request, 'shop_details.html', context)