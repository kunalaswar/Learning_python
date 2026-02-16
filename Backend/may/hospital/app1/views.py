from django.shortcuts import render,redirect
from app1.forms import DoctorForm,PatientForm,AppointmentForm 
from app1.models import Doctor ,Patient,Appointment
from django.urls import reverse

# Create your views here.
def doctoradd(request):
    msg=''
    if request.method == 'POST':
        d=DoctorForm(request.POST)
        if d.is_valid():
            d.save()
            msg = "Doctor Details Added"
            # redirect
    form=DoctorForm()        
    response = render(request,'adddoctor_temp.html',context={'form':form,'msg':msg})
    return response

# def display_adddoctor_temp(request):

def listdoctors(request):
    qs = Doctor.objects.all()
    response= render(request,'listdoctor_temp.html',context={'qs':qs})
    return response
def home(request):
    response= render(request,'base.html',context={})
    return response

# def doctoredit(request,name):
#     d = Doctor.objects.get(name = name)  # this is old data and we have to put here because it is use in two if and elif also 
#     if request.method == "GET":
#         form = DoctorForm(instance=d)
#         response= render(request,'editdoctor_temp.html',context={'form':form})
#         return response
#     elif request.method=='POST':
            # msg = ''
            # form =DoctorForm(request,POST,instance=d)
            # if form.is_valid():
                # form.save()
#^ this is for Edit the Doctor details 
def doctoredit(request,name): #todo - first we are reading the details of doctor 
    d = Doctor.objects.get(name = name)  # this is old data and we have to put here because it is use in two if and elif also
    # msg = ''
    if request.method=='POST':
        form = DoctorForm(request.POST,instance=d) 
        if form.is_valid():
            form.save()
            # msg = 'Doctor Details Updated'
            response=redirect('doctorlist')# view name 
            return response 
    form = DoctorForm(instance=d)        
    response = render(request,'editdoctor_temp.html',context={'form':form})
    return response 

#^ this is for Delete the Doctor details 
def doctordelete(request,name):
    # d = Doctor.objects.get(name = name) # first we read the details 
    # After read we can delete details by using delete keyword 
    # del d #& this is only delete the variable  but not objects 
    d=Doctor.objects.get(name = name)
    d.delete()
    res = redirect('doctorlist')
    return res 

def patientadd(request):
    msg=''
    if request.method=='POST':
        form = PatientForm(request.POST) # we have creating instance of PatientForm populating of patient data
        if form.is_valid():
            form.save()
            msg='patient Details Saved'

    form =PatientForm()        
    res = render(request,'patientadd_temp.html',context={'form':form,'msg':msg})
    return res 

def patientlist(request):
    qs = Patient.objects.all()# Patient.modelmanager.all()
    res = render(request,'listpatient_temp.html',context={'qs':qs})
    return res

def patientedit(request,name): #todo - ethe aapna name cha based var edit karnar nnhe manun eth name ha primary key ghetale aahe 
    # Every thing is same here we just copy and paste here 
    d = Patient.objects.get(name = name)
    if request.method=='POST':
        form = PatientForm(request.POST,instance=d) # here i am trying to populate to PatientForm 
        if form.is_valid():
            form.save()
            response= redirect('patientlist')
            return response 
    form = PatientForm(instance=d)
    response = render(request,'editpatient_temp.html',context={'form':form})
    return response

def patientdelete(request,name):
    p = Patient.objects.get(name=name)
    p.delete()
    # after deleting we have to redirect to same templates 
    res= redirect('patientlist') # patientlist he name = patientlist urls.pyu mafdhe dele aahe 
    return res 

def appointment(request):
    # if the request method is get you have to read the details of patient you have to tread the details of doctor and populate details with in form 
    #todo - i want only doctor name 
    msg = ""
    if request.method=='POST':
        # create model instance
        # a = AppointmentForm(request.POST)
        # if a.is_valid():
        #     a.save()
        d = Doctor.objects.get(name=request.POST.get('doctor'))
        p = Patient.objects.get(name=request.POST.get('patient'))
        date = request.POST.get('date')
        time = request.POST.get('time')
        desc = request.POST.get('desc')

        a = Appointment.objects.create(doctor=d,patient=p,date=date,time=time)#todo-this is a another way to do this / this is another method to do this 
        # a = Appointment.objects.create()
        a.doctor=d
        a.patient=p
        a.date = date
        a.time = time
        a.save()
        msg="Appointment is Conformed "

    qs1 = Doctor.objects.all() #^ all() return all the doctor details along with spelizations and contact
    qs2 = Patient.objects.all()
    res = render(request,'appointment_temp.html',context={'qs1':qs1,'qs2':qs2,'msg':msg})
    return res 

def applist(request):
    qs = Appointment.objects.all()
    res = render(request,'appointmentlist_temp.html',context={'qs':qs})
    return res 







