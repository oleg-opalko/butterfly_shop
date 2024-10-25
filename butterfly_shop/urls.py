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

from account.forms import UserRegisterForm
from account.views import UserLoginView, UserRegisterView, logout
from butterfly_shop import settings
from home.views import index
from shop.views import shop
from shop_details.views import shop_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', logout, name='logout'),
    path('shop/', shop, name='shop'),
    path('product/<slug:slug>/', shop_details, name='shop_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
