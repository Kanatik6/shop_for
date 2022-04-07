from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins, status

from apps.cart.models import (
    CartProduct, 
    Order, 
    Cart
)
from apps.cart.serializers import (
    CartProductSerializer,
    OrderSerializer,
    CartSerializer,
)


class CartReadView(
    GenericViewSet
):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    
    @action(methods=['get',],detail=False)
    def me(self, request, *args, **kwargs):
        cart = self.get_queryset().filter(user=self.request.user.id).first()
        serializer = self.get_serializer(cart)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
            )


class CartProductView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self,request,*args,**kwargs):
        order = self.get_queryset().filter(user=request.user).first()
        serializer = self.get_serializer(order)
        return Response(serializer.data)
