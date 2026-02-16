from django.contrib import admin
from testapp.models import  *# Student,Teacher,ContactInfo1, Student1,Teacher1,Person,Employee,Manager 
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)

# 
admin.site.register(Student1)
admin.site.register(Teacher1)
admin.site.register(ContactInfo1)

#
admin.site.register(Person)
admin.site.register(Employee)
admin.site.register(Manager)

