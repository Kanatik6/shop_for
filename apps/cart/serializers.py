from rest_framework.exceptions import ValidationError
from rest_framework import serializers

from apps.cart.models import Cart,CartProduct
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

        if validated_data["amount"] > product.amount:
            raise ValidationError(detail="items in stock fewer  than you want to buy")

        product.amount -= validated_data["amount"]
        product.save()

        Product = self.Meta.model
        instance = Product._default_manager.create(cart=cart, **validated_data)
        return instance
