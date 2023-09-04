from rest_framework import viewsets
from rest_framework import serializers
from api.models import Market
from api.permissions import IsAdminUserOrReadOnly

# Create your views here.
class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ['id', 'name', 'cnpj']

class Markets(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = [IsAdminUserOrReadOnly]