import time
import requests
import json 

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

print("GET request")

def get_resourse(id=None): 
    data = {}
    if id is not None:
        data = {'id':id}
    resp = requests.get(BASE_URL+END_POINT,data=json.dumps(data))    
    print(resp.status_code) 
    print(resp.json())
get_resourse(3)

time.sleep(10)
print("POST request")
def create_resource():
    new_emp = {
        'eno':107,
        'ename':'Ridhika',
        'esal':22000,
        'eaddr':'Dlehi'
    }
    resp = requests.post(BASE_URL + END_POINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
create_resource()

time.sleep(10)
print("UPDATE Record ")
def update_resourse(id):
    new_emp = {
        'id':id,
        
        'ename':'LILLY',
        'esal':12345,
    }
    resp = requests.post(BASE_URL + END_POINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
update_resourse(9)
time.sleep(10)
print("DELETE Record  ")
def delete_resourse(id):

    jdata = {
        'id':id
    }
    resp = requests.delete(BASE_URL + END_POINT, data=json.dumps(jdata))
    print(resp.status_code)
    print(resp.json())
delete_resourse(11)




