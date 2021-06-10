from django.shortcuts import render
from rest_framework import status
from django.http import Http404,QueryDict
from .serializers import UsersSerializer, AddressSerializer, CategoriesSerializer, OrderDetailsSerializer, ProductsSerializer, OrdersSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Users, Address, Categories, Products, Orders, Order_details


# Create your views here.

#ADDRESS
class IndividualAddress(APIView):
    serializer_class=AddressSerializer
    def get_address(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return Http404()

    def get(self, request,pk,format=None):
        address = self.get_address(pk)
        serializers = self.serializer_class(address)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        address = self.get_address(pk)
        serializers = self.serializer_class(address, request.data)
        if serializers.is_valid():
            serializers.save()
            address_list = serializers.data
            response = {
                'data': {
                    'address': dict(address_list),
                    'status': 'success',
                    'message': 'Address updated successfully',
                }
            }
            return Response(response)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        address = self.get_address(pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddressList(APIView):
    serializer_class=AddressSerializer
    def get(self, request, format=None):
        address=Address.objects.all()
        serializers=self.serializer_class(address, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            address=serializers.data
            response = {
                'data': {
                    'address': dict(address),
                    'status': 'success',
                    'message': 'Address created successfully',
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, format=None):
        address=Address.objects.all()
        serializers=self.serializer_class(address, many=True)
        return Response(serializers.data)

#USERS
class IndividualUsers(APIView):
    serializer_class=UsersSerializer
    def get_users(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Http404()

    def get(self, request,pk,format=None):
        users = self.get_users(pk)
        serializers = self.serializer_class(users)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        users = self.get_users(pk)
        serializers = self.serializer_class(users, request.data)
        if serializers.is_valid():
            serializers.save()
            users_list = serializers.data
            response = {
                'data': {
                    'users': dict(users_list),
                    'status': 'success',
                    'message': 'User updated successfully',
                }
            }
            return Response(response)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        users = self.get_users(pk)
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UsersList(APIView):
    serializer_class=UsersSerializer
    def get(self, request, format=None):
        users=Users.objects.all()
        serializers=self.serializer_class(users, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            users=serializers.data
            response = {
                'data': {
                    'users': dict(users),
                    'status': 'success',
                    'message': 'Users created successfully',
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, format=None):
        users=Users.objects.all()
        serializers=self.serializer_class(users, many=True)
        return Response(serializers.data)
    
#Categories
class IndividualCategories(APIView):
    serializer_class=CategoriesSerializer
    def get_categories(self, pk):
        try:
            return Categories.objects.get(pk=pk)
        except Categories.DoesNotExist:
            return Http404()

    def get(self, request,pk,format=None):
        categories = self.get_categories(pk)
        serializers = self.serializer_class(categories)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        categories = self.get_categories(pk)
        serializers = self.serializer_class(categories, request.data)
        if serializers.is_valid():
            serializers.save()
            categories_list = serializers.data
            response = {
                'data': {
                    'categories': dict(categories_list),
                    'status': 'success',
                    'message': 'User updated successfully',
                }
            }
            return Response(response)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        categories = self.get_categories(pk)
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoriesList(APIView):
    serializer_class=CategoriesSerializer
    def get(self, request, format=None):
        categories=Categories.objects.all()
        serializers=self.serializer_class(categories, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            categories=serializers.data
            response = {
                'data': {
                    'categories': dict(categories),
                    'status': 'success',
                    'message': 'Categories created successfully',
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, format=None):
        categories=Categories.objects.all()
        serializers=self.serializer_class(categories, many=True)
        return Response(serializers.data)

#Orders
class IndividualOrders(APIView):
    serializer_class=OrdersSerializer
    def get_orders(self, pk):
        try:
            return Orders.objects.get(pk=pk)
        except Orders.DoesNotExist:
            return Http404()

    def get(self, request,pk,format=None):
        orders = self.get_orders(pk)
        serializers = self.serializer_class(orders)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        orders = self.get_orders(pk)
        serializers = self.serializer_class(orders, request.data)
        if serializers.is_valid():
            serializers.save()
            orders_list = serializers.data
            response = {
                'data': {
                    'orders': dict(orders_list),
                    'status': 'success',
                    'message': 'Orders updated successfully',
                }
            }
            return Response(response)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        orders = self.get_orders(pk)
        orders.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrdersList(APIView):
    serializer_class=OrdersSerializer
    def get(self, request, format=None):
        orders=Orders.objects.all()
        serializers=self.serializer_class(orders, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            orders=serializers.data
            response = {
                'data': {
                    'orders': dict(orders),
                    'status': 'success',
                    'message': 'Orders created successfully',
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, format=None):
        orders=Orders.objects.all()
        serializers=self.serializer_class(orders, many=True)
        return Response(serializers.data)

#Order_Details
class IndividualOrderDetails(APIView):
    serializer_class=OrderDetailsSerializer
    def get_orderdetails(self, pk):
        try:
            return Order_details.objects.get(pk=pk)
        except Order_details.DoesNotExist:
            return Http404()

    def get(self, request,pk,format=None):
        orderdetails = self.get_orderdetails(pk)
        serializers = self.serializer_class(orderdetails)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        orderdetails = self.get_orderdetails(pk)
        serializers = self.serializer_class(orderdetails, request.data)
        if serializers.is_valid():
            serializers.save()
            orderdetails_list = serializers.data
            response = {
                'data': {
                    'orderdetails': dict(orderdetails_list),
                    'status': 'success',
                    'message': 'OrderDetails updated successfully',
                }
            }
            return Response(response)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        orderdetails = self.get_orderdetails(pk)
        orderdetails.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderDetailsList(APIView):
    serializer_class=OrderDetailsSerializer
    def get(self, request, format=None):
        orderdetails=Order_details.objects.all()
        serializers=self.serializer_class(orderdetails, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            orderdetails=serializers.data
            response = {
                'data': {
                    'orderdetails': dict(orderdetails),
                    'status': 'success',
                    'message': 'OrderDetails created successfully',
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, format=None):
        orderdetails=Order_details.objects.all()
        serializers=self.serializer_class(orderdetails, many=True)
        return Response(serializers.data)

#Products
class IndividualProducts(APIView):
    serializer_class=ProductsSerializer
    def get_products(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            return Http404()

    def get(self, request,pk,format=None):
        products = self.get_products(pk)
        serializers = self.serializer_class(products)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        products = self.get_products(pk)
        serializers = self.serializer_class(products, request.data)
        if serializers.is_valid():
            serializers.save()
            products_list = serializers.data
            response = {
                'data': {
                    'products': dict(products_list),
                    'status': 'success',
                    'message': 'Products updated successfully',
                }
            }
            return Response(response)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        products = self.get_products(pk)
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductsList(APIView):
    serializer_class=ProductsSerializer
    def get(self, request, format=None):
        products=Products.objects.all()
        serializers=self.serializer_class(products, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            products=serializers.data
            response = {
                'data': {
                    'products': dict(products),
                    'status': 'success',
                    'message': 'Products created successfully',
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, format=None):
        products=Products.objects.all()
        serializers=self.serializer_class(products, many=True)
        return Response(serializers.data)
    