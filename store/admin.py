from django.contrib import admin

# Register your models here.
from .models import Product, Brand, Colour, Size, Price

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Colour)
admin.site.register(Size)
admin.site.register(Price)