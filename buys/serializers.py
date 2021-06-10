from rest_framework import serializers
from .models import Users, Address, Categories, Products, Orders, Order_details
from django import forms

class UsersSerializer(serializers.ModelSerializer):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    class Meta:
        model = Users
        fields = ['id', 'username', 'email' ,'password', 'age']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_details
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'



