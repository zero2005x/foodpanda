from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=20)
    venue_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self) -> str:
        return super().__str__()


class shop(models.Model):
    shopID = models.CharField(max_length=25, null=False, primary_key=True)
    shopName = models.CharField(max_length=50, null=False)
    shopAddress = models.CharField(max_length=255, blank=True, default='')
    shopRating = models.FloatField(blank=True, default=0.0)
    shopPhone = models.CharField(max_length=50, blank=True, default='')
    shopDescription = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.shopID


class product(models.Model):
    productID = models.CharField(max_length=25, primary_key=True)
    productName = models.CharField(max_length=50, null=False)
    productPrice = models.IntegerField(null=False, default=0)
    productQuantity = models.IntegerField(null=False, default=0)
    productDescription = models.CharField(
        max_length=255, blank=True, default='')
    productURL = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.productID


class user(models.Model):
    userID = models.CharField(max_length=25, null=False, primary_key=True)
    userPassword = models.CharField(max_length=50, null=False)
    userName = models.CharField(max_length=15, null=False)
    userPhone = models.CharField(max_length=50, blank=True, default='')
    userAddress = models.CharField(max_length=255, blank=True, default='')
    userSex = models.BooleanField(blank=True, default=False)
    userBirthday = models.DateField(blank=True, default='')

    def __str__(self):
        return self.userID


class order(models.Model):
    orderID = models.CharField(max_length=25, null=False, primary_key=True)
    storeID = models.CharField(max_length=150, blank=True, default='')
    customerID =  models.CharField(max_length=150, blank=True, default='')
    orderAccountNumber = models.CharField(max_length=50, blank=True, default='')
    def __str__(self):
        return self.orderID


class manufacturer(models.Model):
    manufacturerID = models.CharField(
        max_length=25, null=False, primary_key=True)
    manufacturerName = models.CharField(max_length=15, null=False)
    manufacturerAddress = models.CharField(
        max_length=255, blank=True, default='')

    def __str__(self):
        return self.manufacturerID


class cap(models.Model):
    capID = models.CharField(max_length=25, null=False, primary_key=True)
    capName = models.CharField(max_length=50, blank=True, default='')
    capProfile = models.CharField(max_length=50, blank=True, default='')
    capMaterial = models.CharField(max_length=50, blank=True, default='')
    capProcess = models.CharField(max_length=50, blank=True, default='')
    capFont = models.CharField(max_length=50, blank=True, default='')
    capPrice = models.IntegerField(default=0)
    capImageURL = models.CharField(max_length=50, blank=True, default='')
    capDescription = models.CharField(max_length=50, blank=True, default='')
    def __str__(self):
        return self.capID


class Customers(models.Model):
    customerID = models.CharField(max_length=50, null=False, primary_key=True)
    customerName = models.CharField(max_length=50, null=False, default='')
    customerPhone = models.CharField(max_length=50, blank=True, default='')
    customerAddress = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.ID


class Drivers(models.Model):
    driverID = models.CharField(max_length=50, null=False, primary_key=True)
    driverName = models.CharField(max_length=50, null=False)
    driverPhone = models.CharField(max_length=50, blank=True, default='')
    driverAddress = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.ID


class Meals(models.Model):
    RESTAURANT = models.CharField(max_length=50, null=False)
    NAME = models.CharField(max_length=50, null=False)
    PRICE = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.RESTAURANT


class OrderDetails(models.Model):
    orderID = models.CharField(max_length=25, null=False, primary_key=True)
    productID = models.CharField(max_length=150, null=True)
    quantity = models.IntegerField(null=False, default=0)
    
    def __str__(self):
        return self.Order


class Orders(models.Model):
    Customer = models.CharField(max_length=25, null=False, primary_key=True)
    Rsestaurant = models.CharField(max_length=50, null=False)
    Driver = models.CharField(max_length=50, null=False)
    Address = models.CharField(max_length=50, null=False)
    Total = models.IntegerField(null=False, default=0)
    Status = models.CharField(max_length=50, null=False)
    PickedAt = models.DateTimeField(null=False)

    def __str__(self):
        return self.Customer

class Store(models.Model):
    storeID = models.CharField(max_length=25, null=False, primary_key=True)
    storeName = models.CharField(max_length=50, null=False)
    storePhone = models.CharField(max_length=50, null=False)
    storeAddress = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.ID


class Restaurants(models.Model):
    ID = models.CharField(max_length=25, null=False, primary_key=True)
    USER = models.CharField(max_length=50, null=False)
    NAME = models.CharField(max_length=50, null=False)
    PHONE = models.CharField(max_length=50, null=False)
    ADDRESS = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.ID
       #Restaurants, Orders, OrderDetails, Meals, Drivers, Customers
