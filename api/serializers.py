from rest_framework import serializers
from TestModel.models import product
from TestModel.models import shop
from TestModel.models import cap
from TestModel.models import Restaurants
from TestModel.models import Orders
from TestModel.models import OrderDetails
from TestModel.models import Meals
from TestModel.models import Drivers
from TestModel.models import Customers
from TestModel.models import Store

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop
        fields = '__all__'

class CapSerializer(serializers.ModelSerializer):
    class Meta:
        model = cap
        fields = '__all__'

#Restaurants, Orders, OrderDetails, Meals, Drivers, Customers
class RestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'

class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = '__all__'

class DriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = '__all__'

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'                      