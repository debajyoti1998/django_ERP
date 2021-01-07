from django.db import models

# Create your models here.
# ----DB model -----
class Products(models.Model):
    name = models.CharField(max_length=30)
    purchase_price = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    sell_price = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    stock= models.DecimalField(max_digits=6, decimal_places=2,default=0)
    image = models.ImageField(upload_to="pics/products/")
    deleted=models.IntegerField(default=0)

# class Products(models.Model):
#     product_name=models.CharField(max_length=30)
#     product_price=models.DecimalField(max_digits=6, decimal_places=2)
#     product_sell_price=models.DecimalField(max_digits=6, decimal_places=2)
#     castonar_name=models.CharField(max_length=255)
#     vandor_name=models.CharField(max_length=255)
#     stock=models.CharField(max_length=20)
#     image=models.ImageField(upload_to="pics/products/")
