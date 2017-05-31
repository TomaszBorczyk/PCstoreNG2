from django.db import models
from django.utils import timezone

class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=100)
    register_date = models.DateField('date_registered', default=timezone.now)

    def __str__(self):
        return self.email
