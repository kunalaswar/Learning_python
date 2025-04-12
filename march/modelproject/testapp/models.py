from django.db import models

# Create your models here.
class Employee(models.Model):   # childclass name (parentclass name): inheritance 
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    salary = models.FloatField()
    eaddr = models.CharField(max_length=30)


# class Employee(models.Model):

#   This means you're creating a class named Employee.
#   It inherits from models.Model, which is Django’s base class for models.
#   This tells Django: “Hey! This class should be saved in the database as a table.”

# eno = models.IntegerField()

# You're creating a field called eno, which stores integer values.
# This becomes a column in the Employee table in your database.


