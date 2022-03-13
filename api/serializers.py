from rest_framework import serializers
from TestModel.models import product
from TestModel.models import shop
from TestModel.models import cap

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop
        fields = '__all__'

class CapSerializer(serializers.ModelSerializer):
    class Meta:
        model = cap
        fields = '__all__'