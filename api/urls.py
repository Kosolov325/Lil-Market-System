from rest_framework import routers
from django.urls import path, include
from api.market import Markets
from api.cart import CartEntries
from api.product import Products

router = routers.DefaultRouter()
router.register(r'markets', Markets)
router.register(r'cart-entries', CartEntries)
router.register(r'products', Products)

urlpatterns = [
    path('', include(router.urls)),
]