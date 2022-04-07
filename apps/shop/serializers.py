from rest_framework import serializers
from apps.shop.models import (
    YearTime, 
    Type,
    Product,
    Raiting,
)


class TypeInSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Type
        fields = [
            'id',
            'name',
        ]


class YearTimeSerializers(serializers.ModelSerializer):
    types = TypeInSerializer(many=True,read_only=True)

    class Meta:
        model = YearTime
        fields = (
            "id", 
            "title",
            'types'
            )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "id",
            'in_stock',
            "image", 
            "price", 
            "title", 
            "content", 
            'year',
            'gender',
            'type',
            'price_for',
            'material',
            'production',
            "raiting",
            )


class TypeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True,read_only=True)

    class Meta:
        model = Type
        fields = (
            'id',
            'name',
            'year_time',
            'products'
        )


class RaitingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Raiting
        fields = (
            'id',
            'title',
            'user',
            'product',
            'value',
        )
        read_only_fields = (
            'user',
        )

    def create(self, validated_data):
        user = self.context["request"].user
        instance = self.Meta.model._default_manager.create(
            user=user, **validated_data
        )
        return instance
