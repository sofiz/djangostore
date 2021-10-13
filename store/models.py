from enum import auto
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import PROTECT



class Collection(models.Model):
    title = models.CharField(max_length=255) # title of the collection charfield must have max_length
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True , related_name='+') # a collection can have multiple products one to many 
    # to solve circular dependency use '' set related_name to + to avoid conflict 

class Promotion(models.Model):
    description = models.CharField(max_length=255) #description of the promotion
    discount = models.FloatField() # discount value


class Product(models.Model):
    title = models.CharField(max_length=255) #product title 
    description = models.TextField() # product description
    price = models.DecimalField(max_digits=6, decimal_places=2) # product price decimal must have max_digits & decimal_places 
    inventory = models.IntegerField() 
    last_update = models.DateTimeField(auto_now_add=True)
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT) # if a collection deleted keep this product
    promotions = models.ManyToManyField(Promotion, related_name='products') # products can heve multiple promotions promotions can have multiple products 

class Costumer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES= [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50 ,unique=True)
    phone = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices = MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_STATUS_PENDING= 'P'
    PAYMENT_STATUS_COMPLETE= 'C'
    PAYMENT_STATUS_FAILED= 'F'
    PAYMENT = [
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAILED,'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=15, choices=PAYMENT, default=PAYMENT_STATUS_PENDING)
    costumer = models.ForeignKey(Costumer, on_delete=models.PROTECT)

class Adress(models.Model):
    street= models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    costumer =  models.OneToOneField(Costumer, on_delete=models.CASCADE,primary_key=True)

class Adress(models.Model):
    street= models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    costumer =  models.ForeignKey(Costumer, on_delete=models.CASCADE)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unitprice = models.DecimalField(max_digits=9, decimal_places=2)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()




