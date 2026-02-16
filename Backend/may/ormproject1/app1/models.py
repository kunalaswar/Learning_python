from django.db import models

# Create your models here.
#! Here we have to create how model one is Employee model and another is Employee IDCard Model 
class Employee (models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    #__str__ is a magic method this is Executed when ever you can convert your object into the string type 
    def __str__(self): # below part is auto generated 
        # return super().__str__()
        return self.name 
    
class EmployeeIDCard(models.Model):
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20 , unique=True)
    issue_date = models.DateField(auto_now_add=True)

    def __str__(self):
        # return super().__str__()
        return f"{self.employee.name} 's ID: {self.card_number}"
    

         