from django.db import models
from carts.models import Cart


# Create your models here.
STATUS_CHOICES = (
    ("started", "started"),
    ("abandoned", "abandoned"),
    ("completed", "completed"),
)


class Order(models.Model):
    order_id = models.CharField(max_length=120, default="default", unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="started")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.order_id
