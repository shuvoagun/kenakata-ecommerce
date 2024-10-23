from django.db import models
from Store.models import Order

# Create your models here.
class ShippingAddress(models.Model):
    TYPE = (
        ('Inside Dhaka', 'Inside Dhaka'),
        ('Outside Dhaka', 'Outside Dhaka'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    type = models.CharField(max_length=20, choices=TYPE)
    address = models.TextField()

    def __str__(self):
        return f"Id:{self.id}, Name:{self.name}, Address:{self.address}"