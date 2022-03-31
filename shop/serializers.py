from rest_framework import serializers
from shop.models import Category, Type, Year, Product


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "id", 
            "title",
            )


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = (
            'id',
            'name',
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
            "category", 
            "slug",
            "stock",
            'year',
            'gender',
            'type',
            )
