from django.contrib import admin
from app1.models import StudentModel
# Register your models here.
class StudentModelAdmin(admin.ModelAdmin):
    # exclude  = ['name','']
    list_display = ['rollno','name','course','fee']
    list_display_links =['rollno','name']
    # exclude = ['rollno','name']
    # fields = ['rollno','name']
admin.site.register(StudentModel,StudentModelAdmin)
