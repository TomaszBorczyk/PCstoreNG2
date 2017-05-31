import uuid
from django.utils import timezone
from django.db import models
from products.models import Product
from users.models import User
# from order_product.models import OrderProduct

class Order(models.Model):
    owner = models.ForeignKey(User, related_name='orders')
    products = models.ManyToManyField(Product)
    name = models.UUIDField(default=uuid.uuid4, unique=True)

    shipping_address = models.CharField(max_length = 200)
    is_ordered = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)
    order_date = models.DateField(default=timezone.now)

    def __str__(self):
        return 'Order id: {}'.format(self.name)
