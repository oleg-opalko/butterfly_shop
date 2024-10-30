from django.contrib import admin

from contacts.models import Contact, ContactUs


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('country', 'address', 'phone')
    search_fields = ('country', 'address', 'phone')
    list_filter = ('country',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactUs, ContactUsAdmin)