from rest_framework import serializers
from TestModel.models import product
from TestModel.models import shop
<<<<<<< HEAD
from TestModel.models import cap
=======
>>>>>>> 937ad22ce3e0cb7808322840627da0d93764810e

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop
<<<<<<< HEAD
        fields = '__all__'

class CapSerializer(serializers.ModelSerializer):
    class Meta:
        model = cap
=======
>>>>>>> 937ad22ce3e0cb7808322840627da0d93764810e
        fields = '__all__'