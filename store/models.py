import base64

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Product(models.Model):
    SHIRT_SIZES = (
        ('XS', 'X-Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'X-Large'),
    )
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    quantity = models.DecimalField(max_digits=3, decimal_places=0)
    # img = models.ImageField(upload_to='images/')

    class Meta:
        db_table = "store_product"

    def __str__(self):
        return f"Name: { self.name } Price: ${ self.price } Size: { self.size } Amount in stock: {self.quantity}"


class Cart(models.Model):
    items=models.TextField(blank=True,null=True)
