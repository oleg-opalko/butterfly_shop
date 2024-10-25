from django.shortcuts import render, get_object_or_404

from shop.models import Product


# Create your views here.

def shop_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    images = [product.main_image, product.additional_image_1, product.additional_image_2, product.additional_image_3]
    context = {
        'product': product,
        'images': images,
    }
    return render(request, 'shop_details.html', context)