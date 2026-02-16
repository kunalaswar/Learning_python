from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal  =models.FloatField()
    eaddr = models.CharField(max_length=128)

# makemigrations and migrate 

# This model class tells Django:
# “I want a database table named Employee with these columns.”


# 2️⃣ Table name (created from model)

# If your app name is testapp:

# testapp_employee 
