from django.urls import re_path, path
from . import views

urlpatterns =[
    path('product/', views.getDataProduct, name = 'product'),
    path('addProduct/', views.addItemProduct, name='addProduct'),
    path('shop/', views.getDataShop, name='shop'),
    path('addShop/', views.addItemShop, name='addShop'),
    path('order/', views.getDataShop, name='order'),
    path('addOrder/', views.addItemShop, name='addOrder'),
    path('shop/', views.getDataShop, name='store'),
    path('addShop/', views.addItemShop, name='addStore'),
    path('cap/', views.getDataCap, name='cap'),
    path('addCap/', views.addItemCap, name='addCap'),
    path('Restaurants/', views.getDataRestaurants, name='Restaurants'),
    path('addRestaurants/', views.addItemRestaurants, name='addRestaurants'),
    path('Orders/', views.getDataOrders, name='Orders'),
    path('addOrders/', views.addItemOrders, name='addOrders'),
    path('OrderDetails/', views.getDataOrderDetails, name='OrderDetails'),
    path('addOrderDetails/', views.addItemOrderDetails, name='addOrderDetails'),
    path('Meals/', views.getDataMeals, name='Meals'),
    path('addMeals/', views.addItemMeals, name='addMeals'),
    path('Drivers/', views.getDataDrivers, name='Drivers'),
    path('addDrivers/', views.addItemDrivers, name='addDrivers'),
    path('Customers/', views.getDataCustomers, name='Customers'),
    path('addCustomers/', views.addItemCustomers, name='addCustomers'),
]

