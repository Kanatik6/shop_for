from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from django_filters import rest_framework as filters

from apps.shop.choises import year_values
from apps.shop.serializers import (
    YearTimeSerializers, 
    TypeSerializer,
    ProductSerializer,
    RaitingSerializer,
    )
from apps.shop.models import (
    Type,
    Product,
    YearTime,
    Raiting,
)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        gender = request.query_params.get('gender')
        age = request.query_params.get('age')
        products = instance.products.all()
        print(gender,age)
        if gender in ['Мальчик', "Девочка"]:
            products = products.filter(gender=gender)
        if age in year_values:
            products = products.filter(year=age)
        
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)


class YearTimeViewSet(ModelViewSet):
    queryset = YearTime.objects.all()
    serializer_class = YearTimeSerializers


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        types = instance.types.all()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data)


class RaitingViewSet(ModelViewSet):
    queryset = Raiting.objects.all()
    serializer_class = RaitingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
