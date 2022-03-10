
from urllib import response
from django.http import HttpResponse
from TestModel.models import Test
from django.views.decorators.csrf import csrf_exempt

def add(request):
    name = request.GET.get('name')
    age  = request.GET.get('age')
    test = Test(name=name, age=age)
    test.save()
    return HttpResponse("<p>The data has been add to database.</p>")

def getAll(request):
    list = Test.objects.all()
    response = "" 
    for var in list:
        response += "<p>" + var.name + " " + str(var.age) + "</p>"
       
    return HttpResponse(response)

def update(request):
    id = request.GET.get("id")
    name = request.GET.get('name')
    test = Test.objects.get(id = id)
    test.name = name
    test.save()
    return HttpResponse("Edit success!")

def delete(request):
    
    id = request.GET.get("id")
    test = Test.objects.get(id = id)
    test.delete()
    return HttpResponse("Delete success")
        
@csrf_exempt
def addVenue(request):
    context = {}
    
    return HttpResponse("Delete success")
