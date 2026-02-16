import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelproject3.settings')
import django
django.setup()

from faker import Faker
fake_obj = Faker() #* create a reference variable to the Faker class

from random import randint
def phonenumbergen():
    d1 = randint(6,9)
    num  = "" + str(d1)
    for i in range(9):
        num = num +str(randint(0,9))
    return int(num)    

from testapp.models import student
def populate_file(n):
    for i in range(n):
        fakerollno = fake_obj.random_int(min=1,max = 999)
        fakename = fake_obj.name()
        fakedob = fake_obj.date()
        fakemarks = fake_obj.random_int(min =1,max = 100)
        fakeemail = fake_obj.email()
        fakephonenumber = phonenumbergen()
        fakeaddress = fake_obj.address()
        student.objects.get_or_create(rollno = fakerollno,name = fakename,dob = fakedob,marks = fakemarks,
                                      email = fakeemail,phonenumber = fakephonenumber,address = fakeaddress)
      #*modulename.property.function 
n = int(input("Enter Number of records :"))
populate_file(n)
print(f"{n} Records inserted successfully..... ")

        
