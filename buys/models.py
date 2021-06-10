from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.CharField(max_length=30)

    def save_users(self):
        self.save()

    def delete_users(self):
        self.delete()

class Address(models.Model):
    location = models.CharField(max_length=30)
    description = models.CharField(max_length=30, null=True)
    phone = models.IntegerField()
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE)

    def save_address(self):
        self.save()

    def delete_address(self):
        self.delete()

class Categories(models.Model):
    title = models.CharField(max_length=50)

    def save_categories(self):
        self.save()

    def delete_categories(self):
        self.delete()

class Products(models.Model):
    title = models.CharField(max_length=30)
    image = CloudinaryField('photos')
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    short_description = models.CharField(max_length=30, null=True)
    category_id = models.ForeignKey(Categories,on_delete=models.CASCADE)

    def save_products(self):
        self.save()

    def delete_products(self):
        self.delete()

class Orders(models.Model):
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)

    def save_orders(self):
        self.save()

    def delete_orders(self):
        self.delete()

class Order_details(models.Model):
    order_id=models.ForeignKey(Orders,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def save_details(self):
        self.save()

    def delete_details(self):
        self.delete()

