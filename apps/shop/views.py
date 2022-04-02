from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.shop.serializers import (
    YearTimeSerializers, 
    TypeSerializer,
    ProductSerializer,
    YearSerializer,
    CommentSerializer,
    )
from apps.shop.models import (
    Type,
    Product,
    YearTime,
    Year,
    Comment,
)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,]


class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class YearTimeViewSet(ModelViewSet):
    queryset = YearTime.objects.all()
    serializer_class = YearTimeSerializers

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        types = instance.types.all()
        serializer = TypeSerializer(types, many=True)
        print(serializer.data)
        return Response(serializer.data)


class YearViewSet(ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
