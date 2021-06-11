from django.contrib import admin
from .models import Users, Address, Categories, Products, Orders, Order_details

# Register your models here.
admin.site.register(Users)
admin.site.register(Address)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Order_details)
