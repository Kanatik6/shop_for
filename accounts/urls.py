from rest_framework.routers import SimpleRouter

from accounts.views import  UserModelViewSet,ProfileView

router = SimpleRouter()

router.register('users',UserModelViewSet,'users')
router.register('profile',ProfileView,'profile')

urlpatterns = router.urls