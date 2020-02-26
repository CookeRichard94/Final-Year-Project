from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Product(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    class Meta:
        db_table = "store_product"

    def __str__(self):
        return f"Name: { self.name } Price: ${ self.price } Size: { self.size }"

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

class Brand(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    name = models.CharField(
        max_length=30,
        help_text="Enter a clothing brand (e.g. Calvin Klein, Tommy Hilfiger etc.)"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name