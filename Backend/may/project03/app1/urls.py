
from django.urls import path
from app1.views import index,products

urlpatterns = [
    path('index/',index),
    path('products/',products)
]
