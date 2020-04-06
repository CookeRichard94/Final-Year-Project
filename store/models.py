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
    img = models.BinaryField(max_length=75)

    class Meta:
        db_table = "store_product"

    def __str__(self):
        return f"Name: { self.name } Price: ${ self.price } Size: { self.size } Amount is stock: {self.quantity}"

    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})

class userProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    description=models.TextField(blank=True,null=True)
    location=models.CharField(max_length=30,blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    is_organizer=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Cart(models.Model):
    items=models.TextField(blank=True,null=True)
