from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import SimpleRouter

from django.urls import path

from apps.accounts.views import RegistrationAPIView, UserModelViewSet,ProfileView

router = SimpleRouter()

router.register('users',UserModelViewSet,'users')
router.register('profile',ProfileView,'profile')


urlpatterns = [
    path('token_refresh/', TokenRefreshView.as_view()),
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
]

urlpatterns +=router.urls