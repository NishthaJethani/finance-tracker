from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


CATEGORY_CHOICES = [
    {'breakfast', 'Breakfast'},
    {'lunch', 'Lunch'},
    ('dinner', 'Dinner'),
    ('snacks', 'Snacks'),
    ('entertainment', 'Entertainment'),
    ('travel', 'Travel'),
]


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return self.category
    