from rest_framework.exceptions import ValidationError
from rest_framework import serializers

from apps.cart.models import Cart,CartProduct,Order
from apps.shop.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    cart_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = (
            "id",
            "total_price",
            "cart_products",
        )


class CartProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartProduct
        fields = (
            "id",
            "product",
            "amount",
            "cart",
            "final_price",
            "price",
            "title",
        )
        read_only_fields = ["cart", "price", "final_price", "title"]

    def create(self, validated_data):
        cart = Cart.objects.filter(user=self.context["request"].user.id).first()
        product = validated_data["product"]

        product.save()

        Product = self.Meta.model
        instance = Product._default_manager.create(cart=cart, **validated_data)
        return instance


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            "id",
            "name",
            "number",
            "address",
            "descriptions",
            "price",
        )
        read_only_fields = ["price"]

    def create(self, validated_data):
        user = self.context["request"].user
        cart = Cart.objects.filter(user=user.id).first()
        cart_products = cart.cart_products.all()

        if cart_products.first() == None:
            raise ValidationError(detail="your cart is empty, fill her and try again")

        instance = self.Meta.model._default_manager.create(
            price=cart.total_price, user=user, **validated_data
        )
        cart_products.delete()
        return instance
