from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from api.models import CartEntry, Product, Wallet
from django.db.models import Sum, F

# Create your views here.
class OwnerOrAdmin(DjangoModelPermissions):
    message = 'Adding entries not allowed.'

    def has_permission(self, request, view):
         return True
    
    def has_object_permission(self, request, view, obj):
            return request.user.is_staff or obj.user == request.user
    
class CartEntrySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = CartEntry
        fields = ['id', 'user', 'product', 'qnt']

class CartEntries(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = CartEntry.objects.all()
    serializer_class = CartEntrySerializer
    permission_classes = [OwnerOrAdmin]

class Cart(APIView):
    """
    A viewset that provides the standard actions
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        entries = request.user.cartentry_set.all()
        total_price = entries.aggregate(total_price=Sum(F('qnt') * F('product__price')))['total_price']
        
        return Response({'subtotal': total_price if None else 0.0})
    
class Purchase(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_staff:
            return Response({'detail': 'Usuários administradores não são autorizados a fazerem compras no site.'}, status=status.HTTP_403_FORBIDDEN)
        wallet = user.wallet
        entries = user.cartentry_set.all()
        if not entries:
            return Response({'detail': "Produtos não foram encontrados no carrinho deste usuário."}, status=status.HTTP_204_NO_CONTENT)
        total_price = entries.aggregate(total_price=Sum(F('qnt') * F('product__price')))['total_price']
        if wallet.amount - total_price >= 0:
            wallet.amount -= total_price
            wallet.save()
            message = f"Compra realizada com sucesso!"
            code = status.HTTP_200_OK
        else:
            message = "Saldo insuficiente para completar a compra."
            code = status.HTTP_400_BAD_REQUEST

        return Response({'detail': message}, status=code)
