from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TrackedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_url = models.URLField()
    name = models.CharField(max_length=255)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    price_history = models.JSONField(default=list)
    