from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Market(models.Model):
    name = models.CharField(max_length=50)
    cnpj =models.CharField(max_length=14)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CartEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qnt = models.IntegerField(default=1,null=False, blank=False)

    def __str__(self):
        return self.user.username

