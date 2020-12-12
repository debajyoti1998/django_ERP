from django.db import models

# Create your models here.
# ----DB model -----
class Products(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="pics/products/")