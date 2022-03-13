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
    shopAddress = models.CharField(max_length=255,blank=True, default='')
    shopRating = models.FloatField(blank=True, default=0.0)
    shopPhone = models.CharField(max_length=50, blank=True, default='')
    shopDescription = models.CharField(max_length=255,blank=True, default='')
    def __str__(self):
        return self.shopID

class product(models.Model):
    productID = models.CharField(max_length=25, null=False, primary_key=True)
    productName = models.CharField(max_length=50, null=False)
    productPrice = models.PositiveIntegerField(null=False, default=0)
    productQuantity =  models.PositiveIntegerField(null=False, default=0)
    productDescription = models.CharField(max_length=255,blank=True, default='')
    productURL = models.CharField(max_length=255,blank=True, default='')
    def __str__(self):
        return self.productID

class user(models.Model):
    userID = models.CharField(max_length=25, null=False, primary_key=True)
    userPassword = models.CharField(max_length=50, null=False)
    userName = models.CharField(max_length=15, null=False)
    userPhone = models.CharField(max_length=50, blank=True, default='')
    userAddress = models.CharField(max_length=255,blank=True, default='')
    userSex = models.BooleanField(blank=True, default=False)
    userBirthday = models.DateField(blank=True, default='')
    def __str__(self):
        return self.userID

class order(models.Model):
    orderID = models.CharField(max_length=25, null=False, primary_key=True)
    orderTime = models.DateTimeField(null=False)
    orderTotal = models.PositiveIntegerField(null=False, default=0)
    def __str__(self):
        return self.orderID

class manufacturer(models.Model):
    manufacturerID =  models.CharField(max_length=25, null=False, primary_key=True)
    manufacturerName = models.CharField(max_length=15, null=False)
    manufacturerAddress = models.CharField(max_length=255,blank=True, default='')
    def __str__(self):
        return self.manufacturerID
<<<<<<< HEAD

class cap(models.Model):
    capID = models.CharField(max_length=25, null=False, primary_key=True)
    capProfile = models.CharField(max_length=50, blank=True, default='')
    capMaterial = models.CharField(max_length=50, blank=True, default='')
    capProcess = models.CharField(max_length=50, blank=True, default='')
    capFront = models.CharField(max_length=50, blank=True, default='')
    capPrice = models.IntegerField(default=0)
    CapImageName = models.CharField(max_length=50, blank=True, default='')
    def __str__(self):
        return self.capID

=======
>>>>>>> 937ad22ce3e0cb7808322840627da0d93764810e
