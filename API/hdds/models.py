from django.db import models
from products.models import Product

class Hdd(Product):
    memory = models.IntegerField(default=1000)
    speed = models.IntegerField(default=7200)
    interface = models.CharField(max_length=20, default='SATA3')

    def __str__(self):
        return self.name
