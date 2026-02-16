from django.db import models

# Create your models here.
class  HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=65)
    title = models.CharField(max_length=65)
    eligibility = models.CharField(max_length=65)
    address  = models.TextField()
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    

