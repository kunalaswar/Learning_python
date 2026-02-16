from django import forms
from app1.models import EmpModel

class EmpForm(forms.ModelForm): #* form name is EmpForm 
    class Meta:
        model=EmpModel
        # fields=['__all__']
        fields=['empno','ename','job','sal']

