from django.contrib import admin

from testapp.models import Employees
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin): # admin is module and ModelAdmin is the class  predefined
    #* there list_display  is a predefined variable is there 
    # list_display = ['eno','ename','esal','eaddr']
    list_display = ['id','eno','ename','esal','eaddr']
    # list_display = ['ename','esal']
1
admin.site.register(Employees,EmployeeAdmin)


