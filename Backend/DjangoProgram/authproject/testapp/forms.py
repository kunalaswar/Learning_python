from django import forms
from django.contrib.auth.models import User
class SignUForm(forms.ModelForm):
    class Meta:
        model =User # model name is User
        fields = ['username','password','email','first_name','last_name',]
