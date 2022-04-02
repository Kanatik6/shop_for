
from django.contrib import admin
from shop.models import (
    Product, 
    YearTime, 
    Type,
    Year,
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', "type", 'stock', 'available', ]
    list_filter = ['available']
    list_editable = ['price', 'stock', 'available', ]

admin.site.register(YearTime)
admin.site.register(Product)
admin.site.register(Type)
admin.site.register(Year)
