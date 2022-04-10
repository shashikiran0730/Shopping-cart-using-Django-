from operator import mod
from platform import mac_ver
from pyexpat import model
from typing import ItemsView, MutableSequence
from unicodedata import decimal
from django.db import models
from matplotlib.pyplot import cla

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
class orderconform(models.Model):
    customeremail=models.CharField(max_length=200)
    Itemid=models.CharField(max_length=200)
    Itemname=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    totalprice=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=100,default="orderplaced")
class previousorders(models.Model):
    customeremail=models.CharField(max_length=200)
    Itemid=models.CharField(max_length=200)
    Itemname=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    totalprice=models.DecimalField(max_digits=10,decimal_places=2)
class adminlogin(models.Model):
    empid=models.IntegerField()
    securitycode=models.IntegerField()
    password=models.CharField(max_length=100)

