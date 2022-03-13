from xml.dom.pulldom import PROCESSING_INSTRUCTION
from html5lib import serialize
from rest_framework.response import Response
from rest_framework.decorators import api_view
from TestModel.models import product
from TestModel.models import cap
from TestModel.models import shop
from . serializers import ProductSerializer
from . serializers import ShopSerializer
from . serializers import CapSerializer
def index(request):
    
    return request

@api_view(['GET'])
def getDataShop(request):
    shop1 = shop.objects.all()
    serializer = ShopSerializer(shop1, many=True)
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
def addItemShop(request):
    serializer = ShopSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addItemCap(request):
    serializer = CapSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def getDataCap(request):
    cap1 = cap.objects.all()
    serializer = CapSerializer(cap1, many=True)
    return Response(serializer.data)
