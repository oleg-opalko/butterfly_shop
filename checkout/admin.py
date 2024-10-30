from django.contrib import admin

from checkout.models import Order, OrderItem


# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('product_name', 'quantity', 'price', 'get_total')
    extra = 0

    def get_total(self, obj):
        return obj.get_total()
    get_total.short_description = 'Total Price'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'created_at', 'updated_at', 'total_order_price')
    list_filter = ('created_at', 'updated_at', 'country')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at', 'total_order_price')
    inlines = [OrderItemInline]

    fieldsets = (
        ('Customer Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'country')
        }),
        ('Order Notes', {
            'fields': ('order_notes',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
        ('Order Summary', {
            'fields': ('total_order_price',)
        }),
    )

    def total_order_price(self, obj):
        items = obj.items.all()
        return sum(item.get_total() for item in items)
    total_order_price.short_description = 'Total Order Price'

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'quantity', 'price', 'get_total')
    search_fields = ('product_name',)

    def get_total(self, obj):
        return obj.get_total()
    get_total.short_description = 'Total Price'

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)