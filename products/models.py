from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=30, default=0.00)
    sale_price = models.DecimalField(decimal_places=2, max_digits=30, blank=True, null=True)
    image = models.ImageField(upload_to='products/images/', null=True)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_price(self):
        return self.price
