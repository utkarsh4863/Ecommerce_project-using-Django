from rest_framework import serializers
from app.models import Product, Cart, OrderPlaced, Customer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'selling_price', 'discounted_price', 'description', 'brand', 'category', 'product_image']

class CustomerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    # Fetch all products where product.user == customer.user
    products = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['id', 'username', 'name', 'locality', 'city', 'zipcode', 'state', 'products']

    def get_products(self, obj):
        user_products = Product.objects.filter(user=obj.user)
        return ProductSerializer(user_products, many=True, context=self.context).data
    

class CartSerializer(serializers.ModelSerializer):
    total_cost = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    total_cost = serializers.ReadOnlyField()

    class Meta:
        model = OrderPlaced
        fields = '__all__'