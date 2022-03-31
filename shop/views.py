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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        types = instance.types.all()
        serializer = TypeSerializer(types, many=True)
        print(serializer.data)
        return Response(serializer.data)


class YearViewSet(ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer
