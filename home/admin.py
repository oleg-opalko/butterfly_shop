from django.contrib import admin
from .models import BannerCollection, ClothingBanner

@admin.register(BannerCollection)
class BannerCollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'description', 'image')
    search_fields = ('title', 'subtitle')
    list_filter = ('title',)

@admin.register(ClothingBanner)
class ClothingBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image')
    search_fields = ('title', 'category__name')
    list_filter = ('category',)

    def get_category_name(self, obj):
        return obj.category.name
    get_category_name.short_description = 'Category'
