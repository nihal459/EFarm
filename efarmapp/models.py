from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_farmer = models.BooleanField(default=False, verbose_name='Is Farmer')
    is_shop = models.BooleanField(default=False, verbose_name='Is Shop')
    name = models.CharField(max_length=100, default='User')
    mobile_number = models.CharField(max_length=20, default='Nil')
    bank_name = models.CharField(max_length=100, default='Nil')
    bank_account_number = models.CharField(max_length=50, default='Nil')
    ifsc_code = models.CharField(max_length=20, default='Nil')
    upi_id = models.CharField(max_length=100, default='Nil')
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    location = models.CharField(max_length=300, default='Nil')
    address = models.TextField(max_length=1000, default='Nil')
    district = models.CharField(max_length=150, default='Nil')
    verified = models.BooleanField(default=False, verbose_name='Is Verified')
    fruits = models.BooleanField(default=False, verbose_name='Fruits')
    vegetables = models.BooleanField(default=False, verbose_name='Vegetables')


    @property
    def imageURL(self):
        try:
            url = self.profile_picture.url
        except:
            url = ''
        return  url
    

    def __str__(self):
        return self.username
    

class Pricechart(models.Model):
    shopid = models.IntegerField(blank=True, null=True)
    shopusername = models.CharField(max_length=255, blank=True, null=True)
    shopname = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(max_length=1000, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    fruits = models.BooleanField(default=False, verbose_name='Fruits')
    vegetables = models.BooleanField(default=False, verbose_name='Vegetables')
    item_name = models.CharField(max_length=255, blank=True, null=True)
    item_perkg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.shopname
    

class Productchart(models.Model):
    farmerid = models.IntegerField(blank=True, null=True)
    farmerusername = models.CharField(max_length=255, blank=True, null=True)
    farmername = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(max_length=1000, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    fruits = models.BooleanField(default=False, verbose_name='Fruits')
    vegetables = models.BooleanField(default=False, verbose_name='Vegetables')
    item_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.farmername
    

class Business(models.Model):
    farmerid = models.IntegerField(blank=True, null=True)
    farmerusername = models.CharField(max_length=255, blank=True, null=True)
    farmername = models.CharField(max_length=255, blank=True, null=True)
    shopid = models.IntegerField(blank=True, null=True)
    shopusername = models.CharField(max_length=255, blank=True, null=True)
    shopname = models.CharField(max_length=255, blank=True, null=True)
    fruits = models.BooleanField(default=False, verbose_name='Fruits')
    vegetables = models.BooleanField(default=False, verbose_name='Vegetables')
    item_name = models.CharField(max_length=255, blank=True, null=True)
    item_kg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    farmer_accept = models.BooleanField(default=False, verbose_name='Farmer Accept')
    shop_accept = models.BooleanField(default=False, verbose_name='Shop Accept')
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_paid = models.BooleanField(default=False, verbose_name='Amount Paid')
    amount_received = models.BooleanField(default=False, verbose_name='Amount Received')
    farmer_delivered = models.BooleanField(default=False, verbose_name='Farmer Delivered')
    shop_received = models.BooleanField(default=False, verbose_name='Shop Received')

    def __str__(self):
        return self.item_name



class Doctor(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
