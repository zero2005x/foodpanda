from django.urls import re_path, path
from . import views

urlpatterns =[
    path('product/', views.getDataProduct, name = 'product'),
    path('addProduct/', views.addItemProduct, name='addProduct'),
    path('shop/', views.getDataShop, name='shop'),
    path('addShop/', views.addItemShop, name='addShop'),
    path('cap/', views.getDataCap, name='cap'),
    path('addCap/', views.addItemCap, name='addCap'),
]