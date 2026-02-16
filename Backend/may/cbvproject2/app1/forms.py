from django import forms
from app1.models import EmpModel
class EmpForm(forms.ModelForm):
    class Meta:
        model = EmpModel
        fields = ['empno','ename','job','sal']
        