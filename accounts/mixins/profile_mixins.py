from rest_framework.response import Response
from rest_framework.decorators import action

from accounts.models import Profile
from accounts.serializers import FavoriteIDSerializer


class AddFavoriteMixin:
    @action(
        methods=['post'],
        detail=False,
        serializer_class=FavoriteIDSerializer
        )
    def add_favorite(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        profile = Profile.objects.filter(user=request.user).first()
        profile.favorites.add(serializer.data['product_id'])
        profile.save()

        return Response({'message':'added'})


class RemoveFavoriteMixin:
    @action(
        methods=['post'],
        detail=False,
        serializer_class=FavoriteIDSerializer
        )
    def remove_favorite(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        profile = Profile.objects.filter(user=request.user).first()
        profile.favorites.remove(serializer.data['product_id'])
        profile.save()

        return Response({'message':'removed'})


class UpdateProfileMixin:
    @action(
    detail=False,
    methods=['put']
    )
    def update_profile(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_queryset().filter(user=request.user).first()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
