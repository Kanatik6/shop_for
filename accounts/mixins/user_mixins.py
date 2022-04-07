from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from accounts.models import Profile
from accounts.serializers import PasswordUpdateSerializer, RegistrationSerializer


class UpdateUserMixin:
    @action(
    detail=False,
    methods=['put']
    )
    def update_user(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = request.user
        email = instance.email

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        if self.get_queryset().filter(email=email).first():
            raise ValidationError('email must be unique')
        profile = Profile.objects.filter(user=instance).first().email_verified = False
        profile.save()

        return Response(serializer.data)


class UpdatePasswordMixin:
    @action(
        detail=False,
        permission_classes = [IsAuthenticated],
        methods=['post'],
        serializer_class=PasswordUpdateSerializer
    )
    def update_password(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not request.user.check_password(serializer.data.get('password')):
            raise ValidationError("the password didn't match")

        request.user.set_password(serializer.data.get('new_password'))
        request.user.save()

        return Response({"message":"password updated"})


class RegistrationUserMixin:
    @action(
        detail=False,
        methods=['post'],
        serializer_class=RegistrationSerializer
    )
    def registration(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
