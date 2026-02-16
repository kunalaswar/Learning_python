from django import forms

class StudentForm(forms.Form):
    name = forms.CharField()  #* Did not mension in forms.py class max_length = 30 or any value we write into the models.py 
    Rollno= forms.IntegerField()
    marks = forms.IntegerField()
    