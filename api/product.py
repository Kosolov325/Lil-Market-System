from rest_framework import viewsets
from rest_framework import serializers
from api.models import Product
from api.permissions import IsAdminUserOrReadOnly

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'market']

class Products(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserOrReadOnly]