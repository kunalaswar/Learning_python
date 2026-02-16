
#todo - We have to Create this file with name with the urls.py 
from django.urls import path
from app1.views import view1,view2

urlpatterns = [path('v1/',view1),
               path('v2/',view2)]
