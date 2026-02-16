"""crudviewproject URL Configuration

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
    path('',EmpListView.as_view(),name= 'listemp'),
    path('update_emp/<pk>/',EmpUpdateView.as_view(),name= 'update_emp'), # .as_view he tayle callable banavate
    path('delete_emp/<pk>/',EmpDeleteView.as_view(),name='delete_emp'),
    path('createemp/',EmpCreateView.as_view(),name='createemp'),
    path('detailemp/<pk>/',EmpDetailsView.as_view(),name='detailemp'), #here i am send request with what Empno it is a primary key na 
    path('listemp1/',EmpListView1.as_view(),name='listemp1'),
    path('listemp2/<str:job>/',EmpListView2.as_view(),name='listemp2'),#  type is str parameter name is job
    path('listemp3/',EmpListView3.as_view(),name = "listemp3"),
    path('showjob/',joblist),
    path('detailemp1/<pk>/',EmpDetailsView1.as_view(),name='detailemp1'),
    path('detailemp4/<pk>/',EmpDetailsView4.as_view(),name='detailemp4'),#^he name aahe he aapan url madhe takato load zala var
    path('test1/',TestTempView.as_view(),name='test1'),
    path('test2/',TestTempView1.as_view(),name='test2'),
    
]
