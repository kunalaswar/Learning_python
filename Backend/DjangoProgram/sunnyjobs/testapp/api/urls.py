from django.urls import path,include
from rest_framework import routers

from testapp.api.views import HydjobsCRUDCBV
router = routers.DefaultRouter()
router.register('hydjobsinfo',HydjobsCRUDCBV)  # by using referemce variable you have to register your urls 
                # this is urls pattern 
urlpatterns = [
    path('',include( router.urls)),
]

# http://127.0.0.1:8000/api/hydjobsinfo/