from django.contrib import admin
from django.urls import path
from app1.views import view1,view2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/',view1),
    path('v2/',view2)
]
