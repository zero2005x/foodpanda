from rest_framework import serializers
from TestModel.models import product
from TestModel.models import shop

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop
        fields = '__all__'