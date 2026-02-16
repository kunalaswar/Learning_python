"""
URL configuration for withrestc3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# # from testapp.views import EmployeeListCreateAPIView,EmployeeRetrieveUpdateAPIView,EmployeeRetrieveDestroyAPIView,EmployeeRetrieveUpdateDestroyAPIView
# from testapp.views import EmployeeListCreateAPIView,EmployeeRetrieveUpdateDestroyAPIView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('api/',EmployeeListAPIView.as_view() ),
#     # path('api/',EmployeeCreateAPIView.as_view() ),
#     # path('api/<int:pk>/',EmployeeRetrieveAPIView.as_view()),
#     # path('api/<int:id>/',EmployeeRetrieveAPIView.as_view()),
#     # path('api/<int:id>/',EmployeeUpdateAPIView.as_view()),
#     # path('api/<int:id>/',EmployeeDestroyAPIView.as_view()),

#     #todo - next video
#     path('api/',EmployeeListCreateAPIView.as_view()),  # Employee List Create Api page we have to see
#     # path('api/<int:id>',EmployeeRetrieveUpdateAPIView.as_view()),  # Employee List Create Api page we have to see

#     # path('api/<int:id>',EmployeeRetrieveDestroyAPIView.as_view()),  # Employee List Create Api page we have to see
#     path('api/<int:id>',EmployeeRetrieveUpdateDestroyAPIView.as_view()),  # Employee List Create Api page we have to see

# ] 

from django.contrib import admin
from django.urls import path
from testapp.views import EmployeeListCreateModelMixin,EmployeeRetrieveUpdateDestroyModelMixin

urlpatterns = [
    path('admin/', admin.site.urls),

    #todo - next video
    path('api/',EmployeeListCreateModelMixin.as_view()),
    path('api/<int:pk>/',EmployeeRetrieveUpdateDestroyModelMixin.as_view()),
    

] 


