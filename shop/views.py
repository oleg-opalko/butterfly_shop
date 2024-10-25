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
    category_slug = request.GET.get('category_slug')
    brand_slug = request.GET.get('brand_slug')
    size = request.GET.get('size')
    min_price = request.GET.get('min')
    max_price = request.GET.get('max')
    color = request.GET.get('color')
    tag = request.GET.get('tag')

    products_list = Product.objects.filter(is_visible=True)

    # Filter for categories, if selected
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_list = products_list.filter(category=category)

    if brand_slug:
        brand = get_object_or_404(Branding, slug=brand_slug)
        products_list = products_list.filter(branding=brand)

    if min_price and max_price:
        products_list = products_list.filter(price__gte=min_price, price__lte=max_price)
    elif min_price:
        products_list = products_list.filter(price__gte=min_price)
    elif max_price:
        products_list = products_list.filter(price__lte=max_price)

    if size:
        size = get_object_or_404(SizeCategory, slug=size)
        products_list = products_list.filter(size=size)

    if color:
        color = get_object_or_404(Color, hex_code=color)
        products_list = products_list.filter(colors=color)

    if tag:
        tag = get_object_or_404(Tag, slug=tag)
        products_list = products_list.filter(tags=tag)


    # Pagination
    paginator = Paginator(products_list, 12)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    # AJAX-call, return only block products
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'includes/shop_product_option.html', {
            'products': products,
        })

    # If this general call, return all content
    context = {
        'categories': CATEGORIES,
        'brands': BRANDS,
        'sizes': SIZES,
        'colors': COLORS,
        'tags': TAGS,
        'products': products,
    }
    return render(request, 'shop.html', context)
