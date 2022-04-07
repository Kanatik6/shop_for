
from django.contrib import admin
from apps.shop.models import (
    Product, 
    YearTime, 
    Type,
    Raiting
)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', "type", 'stock', 'available', ]
    list_filter = ['available']
    list_editable = ['price', 'stock', 'available', ]

admin.site.register(YearTime)
admin.site.register(Raiting)
admin.site.register(Product)
admin.site.register(Type)
