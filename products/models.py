from django.db import models
from PIL import Image


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=30, default=0.00)
    sale_price = models.DecimalField(decimal_places=2, max_digits=30, blank=True, null=True)
    # image = models.ImageField(upload_to='products/images/', null=True)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_price(self):
        return self.price


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/', null=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.title

    # Override the save method
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.width > 150 or img.length > 200:
            output_size = (150, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)
