from django.forms import ModelForm
from app1.models import EmpModel

class EmpForm(ModelForm):
    class Meta:
        model = EmpModel
        fields= ['empno','ename','job','sal']