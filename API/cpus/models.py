from django.db import models
from products.models import Product

class Cpu(Product):
    watts = models.IntegerField(default=100)
    frequency = models.IntegerField(default=3200)
    cache = models.IntegerField(default=6)
    core = models.IntegerField(default=4)
    socket = models.CharField(max_length=10, default='1150')

    def __str__(self):
        return self.name
