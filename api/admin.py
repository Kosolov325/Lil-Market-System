from django.contrib import admin
from api.models import Market, Product, CartEntry

# Register your models here.
admin.site.register(Market)
admin.site.register(Product)
admin.site.register(CartEntry)