
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from TestModel.models import Venue

def index(request):
    if request.user.is_authenticated:
        name=request.user.username
    return render(request, "index.html", locals())

def index1(request):
    context = {}
    context["number"] = "05"
    context["name"] = "Tiffany"
    context["AppName"] = "NoteApp_Variant"
    return render(request, "index1.html", context)

def index3(request):
    context = {}
    context["name"] = "Tiffany"
    views_list = ["Django", "Python", "C++"]
    context["views_list"] = views_list

    views_dic = {"name": "Programer A-Liang", "age": 30}
    context["views_dic"] = views_dic

    score = 61
    context["score"] = score

    empty_list = ["Tiffany"]
    context["empty_list"] = empty_list
    
    context["username_input"] = "username_input"
    context["UserName"] = "UserName"
    return render(request, "index3.html", context)

def tiffany(request):
    context = {}
    context["number"] = "MAPD36"
    context["name"] = "Tiffany"
    context["AppName"] = "NoteAppVariant"
    return render(request, "tiffany.html", context)


def theRealKent(request):
    context = {}
    context["number"] = "MAPD36"
    context["name"] = "Kent Paradise"
    context["AppName"] = "BluetoothApp"
    return render(request, "theRealKent.html", context)
    
@csrf_exempt
def addVenue(request):
    #ontext = {}
    if request.method == "POST":
        form = Venue(request.POST, request.FILES)
        if form.is_valid():
            venue = form.save(commit = False)
            venue.save()
    return render(request, "addVenue.html")

def login(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=name, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return redirect('/index/')
				message = '登入成功！'
			else:
				message = '帳號尚未啟用！'
		else:
			message = '登入失敗！'
	return render(request, "login.html", locals())
	
def logout(request):
	auth.logout(request)
	return redirect('/index/')	

def adduser(request):	
	try:
		user=User.objects.get(username="test")
	except:
		user=None
	if user!=None:
		message = user.username + " 帳號已建立!"
		return HttpResponse(message)
	else:	# 建立 test 帳號			
		user=User.objects.create_user("test","test@test.com.tw","a123456!")
		user.first_name="wen" # 姓名
		user.last_name="lin"  # 姓氏
		user.is_staff=True	# 工作人員狀態
		user.save()
		return redirect('/admin/')

def CFRS(request):
    context = {}
    context["number"] = "MAPD36"
    return render(request, "CFRS.html", context)
