import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sunnyjobs.settings')
import django
django.setup()

from faker import Faker
from random import *
from testapp.models import HydJobs

fake_obj = Faker()

def phonenumbergen():
    d1 = randint(6,9)
    num = ''+str(d1)
    for i in range(9):
        num = num+str(randint(0,9))
    return int(num)    

def populate(n):
    for i in range(n):
        fdate = fake_obj.date()
        fcompany = fake_obj.company()
        ftitle = fake_obj.random_element(elements=('Project Manager', 'Team lead', 'Software Engineer', 'Associate Engineer'))
        feligibility =  fake_obj.random_element(elements=('B.Tech', 'M.Tech', 'MCA', 'Phd', 'IT'))
        faddress = fake_obj.address()
        femail = fake_obj.email()
        fphonenumber = phonenumbergen()
        
        HydJobs.objects.get_or_create(
            date = fdate,
            company = fcompany,
            title = ftitle,
            eligibility = feligibility,
            address = faddress,
            email = femail,
            phonenumber = fphonenumber,
        )

n = int(input("Enter number of  records "))
populate(n)
print(f"{n} record inserted Successfully......")


