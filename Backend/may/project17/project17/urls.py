"""project17 URL Configuration

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
from app1.views import addemp_view,listemp_view,update_view,delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addemp/',addemp_view),
    path('listemp/',listemp_view,name='listemp'),
    path('update_view/<eno>/',update_view), # update le parameter aahe manun 
    path('delete_view/<eno>/',delete_view),


    ]
