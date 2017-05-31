import uuid
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10)
    # id_in_category = models.IntegerField()
    product_code = models.UUIDField(default=uuid.uuid4, unique=True)

    brand = models.CharField(max_length=20, default='NoName')
    price = models.FloatField()
    amount = models.IntegerField(default=10)
    total_rating = models.IntegerField(default=11)

    def __str__(self):
        return self.name
