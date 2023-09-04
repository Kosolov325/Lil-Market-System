from rest_framework import viewsets
from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import CartEntry
from api.product import ProductSerializer

# Create your views here.

class CartEntrySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    product = ProductSerializer(data='product')

    class Meta:
        model = CartEntry
        fields = ['id', 'user', 'product', 'qnt']

class CartEntries(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = CartEntry.objects.all()
    serializer_class = CartEntrySerializer