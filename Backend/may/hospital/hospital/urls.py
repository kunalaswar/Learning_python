"""hospital URL Configuration

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
from django.urls import path
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),   #view name
    path('doctoradd/',doctoradd,name='doctoradd'),
    path('doctorlist/',listdoctors,name = 'doctorlist'),
    path('doctoredit/<name>',doctoredit,name='doctoredit'), #^ view madhe aapan two argument dele aahet namun aaplaye eth name dya lagate 
    path('doctordelete/<name>',doctordelete,name='doctordelete'),
    path('patientadd/',patientadd,name='patientadd'),
    path('patientlist/',patientlist,name='patientlist'),
    
    path('patientedit/<name>',patientedit,name='patientedit'), #^ view madhe aapan two argument dele aahet namun aaplaye eth name dya lagate 
    path('patientdelete/<name>',patientdelete,name='patientdelete'),
    path('appointment/',appointment,name='appointment'),
    path('applist/',applist,name='applist'),

]
