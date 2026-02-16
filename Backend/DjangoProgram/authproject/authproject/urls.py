"""authproject URL Configuration

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
from django.urls import path,include
from testapp.views import home_page_view,java_page_view,python_page_view,aptitude_page_view,signup_view,logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page_view),
    path('java/',java_page_view),
    path('python/',python_page_view),
    path('aptitude/',aptitude_page_view),
    path('accounts/',include('django.contrib.auth.urls')), #^file name is urls aahe setting madala auth aahe bus add kela  
    # path('', include('testapp.urls')),
    path('logout/',logout_view),
    path('signup/',signup_view),

]
