from django.contrib import admin
<<<<<<< HEAD
from .models import Product
=======
from .models import products
>>>>>>> ee5f70b2a57eca1aaa111d23c83862cd244708a5

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "availability")

<<<<<<< HEAD
admin.site.register(Product, ProductAdmin)
=======
admin.site.register(products, ProductAdmin)
>>>>>>> ee5f70b2a57eca1aaa111d23c83862cd244708a5
