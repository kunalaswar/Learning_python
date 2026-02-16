from django.forms import ModelForm
from app1.models import Person
class PersonForm(ModelForm):
    # from this class you have to Create another class which is Meta to bind with this 
    # how you define models class with the Help of meta class 
    class Meta:
        model = Person
        fields=['name','image','file']

    
