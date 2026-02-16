from django.db import models

# Create your models here.
class EmpModel(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=25)
    job = models.CharField(max_length=15)
    sal = models.FloatField()
    class Meta:   #* if we dont define a Meta Class it will be 
        db_table='emp' #todo- we are refering to emp table that is present inside of dbtest database


         