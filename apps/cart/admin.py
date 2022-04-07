from django.contrib import admin

from apps.cart.models import (
    Cart,
    CartProduct,
    Order
)

admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Order)
