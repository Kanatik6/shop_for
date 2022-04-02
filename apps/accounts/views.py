from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,status,mixins
from rest_framework.decorators import action

from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.urls import reverse

from secrets import token_hex

from apps.accounts.serializers import UserSerializer, RegistrationSerializer,ProfileSerializer
from apps.accounts.constants import URL
from apps.accounts.models import Profile
from apps.accounts.permissions import VerifiedEmail


User = get_user_model()

class UserModelViewSet(
    GenericViewSet
    ):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
    @action(
        detail=False,
        methods=['get']
        )
    def activate_email(self, request, *args, **kwargs):
        confirmation_token = request.query_params.get('confirmation_token', '')
        user = request.user

        if user is None:
            return Response(
                'User not found', 
                status=status.HTTP_400_BAD_REQUEST
                )
        if not default_token_generator.check_token(user, confirmation_token):
            print(default_token_generator.check_token(user, confirmation_token))
            print(confirmation_token)
            return Response(
                'Token is invalid or expired. Please request another confirmation email by signing in.', 
                status=status.HTTP_400_BAD_REQUEST
                )

        user.profile.email_verified = True
        user.profile.save()
        return Response('Email successfully confirmed')

    @action(
        detail=False,
        permission_classes = [IsAuthenticated],
        methods=['get']
        )
    def send_token(self,request, *args, **kwargs):
        activate_link_url = URL +reverse('users-activate-email')
        confirmation_token = default_token_generator.make_token(request.user)
        activation_link = f'{activate_link_url}?user_id={request.user.id}&confirmation_token={confirmation_token}'
        
        send_mail(
        subject='Подтверждение по почте!',
        message=f"Перейдите по ссылке чтобы подтвержить свою почту на сайте BabyShop {activation_link}",
        from_email=None,
        recipient_list=[request.user.email]
        )

        return Response({'message':f'Сообщение отправлено на email {request.user.email}'})
    
    @action(
        detail=False,
        permission_classes = [IsAuthenticated,VerifiedEmail],
        methods=['get']
    )
    def send_new_password(self,request,*args,**kwargs):
        new_password = token_hex(20)

        send_mail(
        subject='Новый пароль!',
        message=f"Ваш новый пароль - {new_password}",
        from_email=None,
        recipient_list=[request.user.email]
        )

        request.user.set_password(new_password)
        request.user.save()

        return Response({'message':f'Сообщение отправлено на email {request.user.email}'})


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProfileView(
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        profile = self.get_queryset().filter(user=request.user).first()
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

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
