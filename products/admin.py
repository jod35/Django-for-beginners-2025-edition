from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    list_per_page = 10
    list_filter = ['created_at']
    ordering = ['-created_at']

admin.site.register(Product, ProductAdmin)