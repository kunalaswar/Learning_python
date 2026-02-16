from django.db import models

# Create your models here.
#
class Person(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="images") #todo- upload_to is a predefined varible Where you want to upload the image  AND this Upoadding is Done into the Media folder 
    file = models.FileField(upload_to='files/')

