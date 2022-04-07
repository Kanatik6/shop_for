from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins

from django.contrib.auth import get_user_model

from accounts.models import Profile
from accounts.mixins.user_mixins import (
    UpdateUserMixin,
    UpdatePasswordMixin,
    RegistrationUserMixin,
)
from accounts.mixins.profile_mixins import (
    AddFavoriteMixin,
    UpdateProfileMixin,
    RemoveFavoriteMixin
)
from accounts.serializers import (
    UserSerializer,
    ProfileSerializer
)

User = get_user_model()


class UserModelViewSet(
    GenericViewSet,
    UpdateUserMixin,
    UpdatePasswordMixin,
    RegistrationUserMixin,
    ):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer



class ProfileView(
    AddFavoriteMixin,
    RemoveFavoriteMixin,
    UpdateProfileMixin,
    mixins.ListModelMixin,
    GenericViewSet
    ):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        profile = self.get_queryset().filter(user=request.user).first()
        serializer = self.get_serializer(profile)
        return Response(serializer.data)
