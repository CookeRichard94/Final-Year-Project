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
        return reverse('student_edit', kwargs={'pk': self.pk})