from django.forms import ModelForm
from app1.models import Doctor
from app1.models import Patient
from app1.models import Appointment

class DoctorForm(ModelForm):
    class Meta: # here is write Meta means i have to include all the field 
        model=Doctor
        fields ='__all__' # we write here __all__ beacuse we want to include all the field 

class PatientForm(ModelForm):
    class Meta:
        model=Patient
        fields = '__all__'
class AppointmentForm(ModelForm):
    class Meta:
        model=Appointment 
        fields = '__all__'

