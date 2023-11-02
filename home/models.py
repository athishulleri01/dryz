# from django.db import models
from django.db import models

from accounts.models import CustomUser
from order.models import Order
from product.models import ProductVariant


# Create your models here.

class UserWallet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    transaction = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    def __str__(self):
        return f'{self.user.username} amount {self.amount}'