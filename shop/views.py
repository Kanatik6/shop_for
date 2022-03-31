from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shop.serializers import (
    CategorySerializers, 
    TypeSerializer,
    ProductSerializer,
    YearSerializer
    )
from shop.models import (
    Type,
    Product,
    Category,
    Year,
)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class YearViewSet(ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer
