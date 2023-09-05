from django.contrib import admin
from api.models import Market, Product, CartEntry, Wallet

# Register your models here.
admin.site.register(Market)
admin.site.register(Product)
admin.site.register(CartEntry)
admin.site.register(Wallet)