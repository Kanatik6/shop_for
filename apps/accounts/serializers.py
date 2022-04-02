from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.cart.serializers import CartSerializer,ProductSerializer
from apps.accounts.models import Profile

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class ProfileSerializer(serializers.ModelSerializer):
    favorites = ProductSerializer(many=True,read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Profile
        fields = (
            'id',
            'email_verified',
            'delivery_address',
            'billing_address',
            'favorites',
            'user',
        )
        read_only_fields = [
            'user',
            'email_verified'
        ]


class FavoriteIDSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
