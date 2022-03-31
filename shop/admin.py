
from django.contrib import admin
from shop.models import (
    Product, 
    Category, 
    Type,
    Year,
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', "type", 'stock', 'available', ]
    list_filter = ['available']
    list_editable = ['price', 'stock', 'available', ]

admin.site.register(Category)
# admin.site.register(Product, ProductAdmin)
admin.site.register(Type)
admin.site.register(Year)
