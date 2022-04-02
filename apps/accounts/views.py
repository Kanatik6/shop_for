from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,mixins

from django.contrib.auth import get_user_model

from apps.accounts.models import Profile
from apps.accounts.mixins.user_mixins import (
    SendTokenMixin,
    UpdateUserMixin,
    ActivateEmailMixin,
    SendNewPasswordMixin
)
from apps.accounts.mixins.profile_mixins import (
    AddFavoriteMixin,
    UpdateProfileMixin,
    RemoveFavoriteMixin
)
from apps.accounts.serializers import (
    UserSerializer,
    RegistrationSerializer,
    ProfileSerializer
)

User = get_user_model()


class UserModelViewSet(
    GenericViewSet,
    SendNewPasswordMixin,
    SendTokenMixin,
    UpdateUserMixin,
    ActivateEmailMixin
    ):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


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

