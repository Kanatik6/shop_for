from rest_framework.routers import SimpleRouter

from apps.shop.views import (
    ProductViewSet,
    TypeViewSet,
    YearTimeViewSet,
    YearViewSet
)

router = SimpleRouter()

router.register('products',ProductViewSet,basename='product')
router.register('type',TypeViewSet,basename='type')
router.register('year',YearViewSet,basename='year')
router.register('year_time',YearTimeViewSet,basename='year_time')


urlpatterns = []
urlpatterns += router.urls
