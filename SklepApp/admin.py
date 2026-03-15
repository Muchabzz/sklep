from django.contrib import admin
from .models import products

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "availability")

admin.site.register(products, ProductAdmin)