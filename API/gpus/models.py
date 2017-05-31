from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from products.models import Product

class Gpu(Product):
    vram = models.IntegerField(default=8000)
    core_clock = models.IntegerField(default=1500)
    memory_clock = models.IntegerField(default=4000)
    watts = models.IntegerField(default=500)
    ram_memory = models.CharField(max_length=10, default='GDDR4')

    def __str__(self):
        return self.name
