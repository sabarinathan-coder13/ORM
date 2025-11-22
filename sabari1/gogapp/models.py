
from django.db import models
from django.contrib import admin
class Product(models.Model):
    ProductName=models.CharField(primary_key=True,max_length=10)
    PBrand=models.CharField(max_length=18)
    PID=models.CharField(max_length=26)
    Product_MRP=models.CharField(max_length=12)
    PType=models.CharField(max_length=15)
    manuf_date=models.DateField()

class ProductAdmin(admin.ModelAdmin):
    list_display=["ProductName","PBrand","Product_MRP","PID","manuf_date"]

