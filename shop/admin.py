from django.contrib import admin

from shop.models import Category, Branding, SizeCategory, Color, Product, Tag

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Branding)
class BrandingAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SizeCategory)
class SizeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hex_code', 'created_at', 'updated_at')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'branding', 'price', 'is_visible', 'is_featured', 'created_at')
    list_editable = ('is_visible', 'is_featured')
    list_filter = ('category', 'branding', 'is_visible', 'is_featured', 'created_at')
    search_fields = ('name', 'category__name', 'branding__name')
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('size', 'colors', 'tags')

