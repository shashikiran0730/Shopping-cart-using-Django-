from typing import ItemsView, MutableSequence
from django.db import models

class product(models.Model):
    Itemid=models.CharField(max_length=200)
    Itemname=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    imageurl=models.CharField(max_length=2000)
    description=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)


class mycart(models.Model):
    customeremail=models.CharField(max_length=200)
    Itemid=models.CharField(max_length=200)
    Itemname=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    imageurl=models.CharField(max_length=2000)
    description=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
