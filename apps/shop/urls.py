from rest_framework.routers import SimpleRouter

from apps.shop.views import (
    ProductViewSet,
    TypeViewSet,
    YearTimeViewSet,
    RaitingViewSet,
)

router = SimpleRouter()

router.register('products',ProductViewSet,basename='product')
router.register('types',TypeViewSet,basename='type')
router.register('year_times',YearTimeViewSet,basename='year_time')
router.register('comments',RaitingViewSet,basename='comment')


urlpatterns = []
urlpatterns += router.urls
