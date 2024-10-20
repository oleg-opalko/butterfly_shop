from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, get_object_or_404

from shop.models import Category, Branding, SizeCategory, Color, Tag, Product


# Create your views here.

CATEGORIES = Category.objects.annotate(product_count=Count('products')).filter(is_visible=True)
BRANDS = Branding.objects.filter(is_visible=True)
SIZES = SizeCategory.objects.filter(is_visible=True)
COLORS = Color.objects.all()
TAGS = Tag.objects.all()

def shop(request):

    products_list = Product.objects.filter(is_visible=True)
    paginator = Paginator(products_list, 12)

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'categories': CATEGORIES,
        'brands': BRANDS,
        'sizes': SIZES,
        'colors': COLORS,
        'tags': TAGS,
        'products': products,
    }
    return render(request, 'shop.html', context)

def product_list_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products_list = Product.objects.filter(category=category, is_visible=True)

    paginator = Paginator(products_list, 12)

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'category': category,
        'products': products,
        'categories': CATEGORIES,
        'brands': BRANDS,
        'sizes': SIZES,
        'colors': COLORS,
        'tags': TAGS,
    }

    return render(request, 'shop.html', context)