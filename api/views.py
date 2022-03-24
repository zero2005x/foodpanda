from xml.dom.pulldom import PROCESSING_INSTRUCTION
from html5lib import serialize
from rest_framework.response import Response
from rest_framework.decorators import api_view

#Restaurants, Orders, OrderDetails, Meals, Drivers, Customers

from TestModel.models import Restaurants
from TestModel.models import Orders
from TestModel.models import OrderDetails
from TestModel.models import Meals
from TestModel.models import Drivers
from TestModel.models import Customers
from TestModel.models import product
from TestModel.models import order
from TestModel.models import cap
from TestModel.models import shop
from TestModel.models import Store

#Restaurants, Orders, OrderDetails, Meals, Drivers, Customers
from . serializers import OrderSerializer
from . serializers import RestaurantsSerializer
from . serializers import OrdersSerializer
from . serializers import OrderDetailsSerializer
from . serializers import MealsSerializer
from . serializers import DriversSerializer
from . serializers import CustomersSerializer

from . serializers import ProductSerializer
from . serializers import ShopSerializer
from . serializers import CapSerializer
from . serializers import ProductSerializer
from . serializers import ShopSerializer
from . serializers import StoreSerializer

def index(request):
    return request

@api_view(['GET'])
def getDataOrder(request):
    order1 = order.objects.all()
    serializer = OrderSerializer(order1, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItemOrder(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def getDataShop(request):
    shop1 = shop.objects.all()
    serializer = ShopSerializer(shop1, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addItemShop(request):
    serializer = ShopSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getDataProduct(request):
    product1 = product.objects.all()
    serializer = ProductSerializer(product1, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItemProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addItemCap(request):
    serializer = CapSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getDataCap(request):
    cap1 = cap.objects.all()
    serializer = CapSerializer(cap1, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addItemRestaurants(request):
    serializer = RestaurantsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getDataRestaurants(request):
    Restaurants1 = Restaurants.objects.all()
    serializer = RestaurantsSerializer(Restaurants1, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItemOrders(request):
    serializer = OrdersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getDataOrders(request):
    Orders1 = Orders.objects.all()
    serializer = OrdersSerializer(Orders1, many=True)
    return Response(serializer.data)
 


@api_view(['POST'])
def addItemOrderDetails(request):
    serializer = OrderDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getDataOrderDetails(request):
    OrderDetails1 = OrderDetails.objects.all()
    serializer = OrderDetailsSerializer(OrderDetails1, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItemMeals(request):
    serializer = MealsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getDataMeals(request):
    Meals1 = Meals.objects.all()
    serializer = MealsSerializer(Meals1, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addItemDrivers(request):
    serializer = DriversSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getDataDrivers(request):
    Drivers1 = Drivers.objects.all()
    serializer = DriversSerializer(Drivers1, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItemCustomers(request):
    serializer = CustomersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getDataCustomers(request):
    Customers1 = Customers.objects.all()
    serializer = CustomersSerializer(Customers1, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItemStore(request):
    serializer = StoreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getDataStore(request):
    Store1 = Store.objects.all()
    serializer = StoreSerializer(Store1, many=True)
    return Response(serializer.data)
