from django.db import models
from products.models import Product

class Ram(Product):
    memory = models.IntegerField(default='8')
    frequency = models.IntegerField(default='2400')
    latency = models.CharField(max_length=10, default='CL11')
    ram_type = models.CharField(max_length=10, default='DDR3')

    def __str__(self):
        return self.name
