"""
URL configuration for butterfly_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from itertools import product

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import contacts
from account.forms import UserRegisterForm
from account.views import UserLoginView, UserRegisterView, logout
from butterfly_shop import settings
from checkout.views import checkout, order_create, order_confirmation
from contacts.views import contact
from home.views import index
from shop.views import shop
from shop_details.views import shop_details
from shopping_cart.views import cart, add_to_cart, update_cart_item, remove_cart_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', logout, name='logout'),
    path('shop/', shop, name='shop'),
    path('product/<slug:slug>/', shop_details, name='shop_details'),
    path('cart/', cart, name='cart'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('update-cart-item/', update_cart_item, name='update_cart_item'),
    path('remove-cart-item/', remove_cart_item, name='remove_cart_item'),
    path('checkout/', checkout, name='checkout'),
    path('order-create/', order_create, name='order_create'),
    path('order-confirmation', order_confirmation, name='order_confirmation'),
    path('contacts/', contact, name='contacts'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# else:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
