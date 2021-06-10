from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    #Address
    path('api/address/', views.AddressList.as_view(), name='address'),
    path('api/address/update/<int:pk>/',views.IndividualAddress.as_view()),
    path('api/address/delete/<int:pk>/',views.IndividualAddress.as_view()),

    #Users
    path('api/users/', views.UsersList.as_view(), name='neighborhood'),
    path('api/users/update/<int:pk>/',views.IndividualUsers.as_view()),
    path('api/users/delete/<int:pk>/',views.IndividualUsers.as_view()),

    #Orders
    path('api/orders/', views.OrdersList.as_view(), name='neighborhood'),
    path('api/orders/update/<int:pk>/',views.IndividualOrders.as_view()),
    path('api/orders/delete/<int:pk>/',views.IndividualOrders.as_view()),

    #Categories
    path('api/categories/', views.CategoriesList.as_view(), name='neighborhood'),
    path('api/categories/update/<int:pk>/',views.IndividualCategories.as_view()),
    path('api/categories/delete/<int:pk>/',views.IndividualCategories.as_view()),

    #OrderDetails
    path('api/orderdetails/', views.OrderDetailsList.as_view(), name='neighborhood'),
    path('api/orderdetails/update/<int:pk>/',views.IndividualOrderDetails.as_view()),
    path('api/orderdetails/delete/<int:pk>/',views.IndividualOrderDetails.as_view()),

    #Products
    path('api/products/', views.ProductsList.as_view(), name='neighborhood'),
    path('api/products/update/<int:pk>/',views.IndividualProducts.as_view()),
    path('api/products/delete/<int:pk>/',views.IndividualProducts.as_view()),

]