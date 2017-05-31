from django.db import models
from products.models import Product

class Ssd(Product):
    memory = models.IntegerField(default=250)
    read = models.IntegerField(default=500)
    write = models.IntegerField(default=400)
    interface = models.CharField(max_length=10, default='SATA3')

    def __str__(self):
        return self.name
