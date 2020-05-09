from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to="product_image", blank=True)

    class Meta:
        db_table = "store_product"

    def __str__(self):
        return f"Name: { self.name } Price: ${ self.price } Size: { self.size } Amount in stock: {self.quantity} Image: {self.image}"


class Cart(models.Model):
    items=models.TextField(blank=True,null=True)

