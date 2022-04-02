from rest_framework import serializers
from apps.shop.models import (
    YearTime, 
    Type, 
    Year, 
    Product,
    Comment,
)


class YearTimeSerializers(serializers.ModelSerializer):

    class Meta:
        model = YearTime
        fields = (
            "id", 
            "title",
            )


class YearSerializer(serializers.ModelSerializer):

    class Meta:
        model = Year
        fields = (
            'id',
            'year',
        )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "id", 
            "image", 
            "price", 
            "title", 
            "content", 
            "slug",
            "stock",
            'year',
            'gender',
            'type',
            )


class TypeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Type
        fields = (
            'id',
            'name',
            'year_time',
            'products'
        )


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = (
            'id',
            'title',
            'user',
            'product',
        )
