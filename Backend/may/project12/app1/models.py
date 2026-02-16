from django.db import models

# Create your models here. #! Model means Table
class StudentModel(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    fee = models.FloatField()
    
