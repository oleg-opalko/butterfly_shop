from django.db.models import Count
from django.shortcuts import render
from home.models import BannerCollection
from shop.models import Product


# Create your views here.
def index(request):
    collections = BannerCollection.objects.all()

    products = Product.objects.annotate(num_items=Count('id')).order_by('?')[:12]

    context = {
        'collections': collections,
        'products': products
    }
    return render(request, 'index.html', context)