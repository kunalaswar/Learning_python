from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
class EmployeeCRUDCBV(viewsets.ModelViewSet):  # http://127.0.0.1:8000/api/ and http://127.0.0.1:8000/api/1/
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

# a3VuYWw6MTIz 
