"""foodPanda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import include, re_path

import api
from . import views

from api.views import getDataProduct

from . import testdb
from TestModel.models import Test

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('index/', views.index),
    re_path('login/', views.login),
    re_path('logout/', views.logout),
    re_path('adduser/', views.adduser),
    re_path('index1/', views.index1),
    re_path('index3/', views.index3),
    re_path('tiffany/', views.tiffany),
    re_path('theRealKent/', views.theRealKent),
    re_path('CFRS/', views.CFRS),
    re_path('addVenue/', views.addVenue),
    re_path(r'db/add$', testdb.add),
    re_path('db/getall', testdb.getAll),
    re_path('db/update', testdb.update),
    re_path('db/delete', testdb.delete),
    re_path('api/', include('api.urls')),

    re_path('',views.index,name='index'),
    re_path('',views.login,name='login'),
    re_path('',views.logout,name='logout'),
    re_path('',views.adduser,name='adduser'),
    re_path('',views.index1,name='index1'),
    re_path('',views.tiffany,name='tiffany'),
    re_path('',views.theRealKent,name='theRealKent'),
    re_path('',views.index3,name='index3'),
    re_path('',views.addVenue,name='addVenue'),
    re_path('',views.CFRS,name='CFRS'),
    
    
]
