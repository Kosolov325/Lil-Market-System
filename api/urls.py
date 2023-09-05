from rest_framework import routers
from django.urls import path, include
from api.market import Markets
from api.cart import Cart, CartEntries, Purchase
from api.product import Products
from api.authentication import RegisterView, LoginView, LogoutAPIView

router = routers.DefaultRouter()
router.register(r'markets', Markets)
router.register(r'cart-entries', CartEntries)
router.register(r'products', Products)

urlpatterns = [
    path('', include(router.urls)),
    path('cart/', Cart.as_view()),
    path('cart/purchase/', Purchase.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
]