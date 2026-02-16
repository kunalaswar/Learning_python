from django.db import models
# Create your models here.

#^ 43 19th july 

class Course(models.Model):
    name = models.CharField(primary_key=True,max_length=30)
    fee = models.FloatField()
    # here Meta M is always capital
    class Meta:
        db_table = "course"

class Student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    class Meta:
        db_table = "student"
