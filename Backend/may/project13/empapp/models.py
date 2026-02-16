from django.db import models

# Create your models here.
class EmpModel(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=25)
    job = models.CharField(max_length=15)
    sal = models.FloatField()
    class Meta: #! Here M is the capital for Meta that means we rename your table name with 'emp' 
        db_table = 'emp'
