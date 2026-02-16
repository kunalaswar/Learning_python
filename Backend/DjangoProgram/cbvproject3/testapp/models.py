from django.db import models

# Create your models here.
from django.urls import reverse
class Company(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    ceo= models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse("detail",kwargs={"pk":self.pk})
    
    #  def get_absolute_url(self):
    #     # This is a SPECIAL METHOD that tells Django where to redirect after
    #     # creating/updating this object
    #     # Used automatically by CreateView, UpdateView
        
    #     return reverse("detail", kwargs={"pk": self.pk})
    #     # You're creating a URL dynamically
    #     # reverse() = converts URL name to actual URL path
    #     # "detail" = name of the URL pattern
    #     # kwargs={"pk": self.pk} = passing the object's primary key (id)