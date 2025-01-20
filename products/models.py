from django.db import models



class Products(models.Model):
    product_name = models.CharField(max_length=100,null=True,blank=True)
    brand = models.CharField(max_length=100,null=True,blank=True)
    price = models.FloatField()