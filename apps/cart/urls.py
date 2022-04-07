from rest_framework.routers import SimpleRouter

from apps.cart.views import (
    OrderViewSet,
    CartReadView,
    CartProductView
)

router = SimpleRouter()

router.register('order',OrderViewSet,basename='order')
router.register('cart',CartReadView,basename='cart')
router.register('cart_product',CartProductView,basename='cart_product')


urlpatterns = []
urlpatterns += router.urls
