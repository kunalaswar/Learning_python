from django.db import models

# Create your models here.
from django.urls import reverse
class Book(models.Model):# Creates a model named Book & Django converts this into a database table
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    pages = models.IntegerField()
    price = models.FloatField()

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

        #---------------------------------------
 # User submits form
#      ↓
# Book object saved
#      ↓
# get_absolute_url() called
#      ↓
# reverse('detail', pk)
#      ↓
# /5/
#      ↓
# BookDetailView     ↓
# Book detail page shown

