from rest_framework.routers import SimpleRouter

from shop.views import (
    ProductViewSet,
    TypeViewSet,
    CategoryViewSet,
    YearViewSet
)

router = SimpleRouter()

router.register('models',ProductViewSet,basename='product')
router.register('type',TypeViewSet,basename='type')
router.register('year',YearViewSet,basename='year')
router.register('category',CategoryViewSet,basename='category')


urlpatterns = []
urlpatterns += router.urls
