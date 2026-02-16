from django.db import models

# Create your models here.
class Course(models.Model):
    cname =models.CharField(max_length=20)#,primary_key=True)
    fee = models.FloatField()
    def __str__(self):
        # return super().__str__()
        return f'{self.cname},{self.fee}'



class Student(models.Model):
    name =models.CharField(max_length=20)
    # rollno = models.IntegerField(primary_key=True)
    course = models.ManyToManyField(Course,related_name='students') # here we add related_name keyword argument
    
    def __str__(self):
        #
        return f'{self.name}'
# Here:
# 👉 Course is the model class you defined above
# You are telling Django:

# One student can join many courses
# One course can have many students    
