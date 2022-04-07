from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.shop.serializers import ProductSerializer
from accounts.models import Profile

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'password', 'password2','email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise ValidationError("passwords didn't match")
        if User.objects.filter(email=attrs.get('email')).first():
            raise ValidationError('email must be unique')
        return attrs

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username','email']


class ProfileSerializer(serializers.ModelSerializer):
    favorites = ProductSerializer(many=True,read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Profile
        fields = (
            'id',
            'full_name',
            'username',
            'delivery_address',
            'billing_address',
            'favorites',
            'user',
        )


class FavoriteIDSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()


class PasswordUpdateSerializer(serializers.Serializer):
    password = serializers.CharField()
    new_password = serializers.CharField()
    new_password2 = serializers.CharField()
    
    def validate(self, attrs):
        if attrs.get('new_password') != attrs.get('new_password2'):
            raise ValidationError("passwords didn't match")
        return attrs