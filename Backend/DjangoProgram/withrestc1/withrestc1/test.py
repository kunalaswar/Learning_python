# from datetime import date
# import requests
# import json 

# BASE_URL = 'http://127.0.0.1:8000/'
# END_POINT = 'api/'

# # def delete_resourse(id):

# #     jdata = {
# #         'id':id
# #     }
# #     resp = requests.delete(BASE_URL + END_POINT, data=json.dumps(jdata))
# #     print(resp.status_code)
# #     print(resp.json())
# # delete_resourse(5)


# # def update_resourse(id):
# #     new_emp = {
# #         'id':id,
# #         'eno':300,
# #         'ename':'Sunnypaa',
# #         'esal':22000,
# #         'eaddr':'Chennai'
# #     }
# #     resp = requests.post(BASE_URL + END_POINT, data=json.dumps(new_emp))
# #     print(resp.status_code)
# #     # print(resp.json())
# # update_resourse(2)



# # def create_resource():
# #     new_emp = {
# #         'eno':105,
# #         'ename':'Pinny',
# #         'esal':18000,
# #         'eaddr':'Vja'
# #     }
# #     resp = requests.post(BASE_URL + END_POINT, data=json.dumps(new_emp))
# #     print(resp.status_code)
# #     print(resp.json())
# # create_resource()
    
# # def get_resourse(id=None): #id =3 if 
# #     data = {}
# #     if id is not None:
# #         data = {'id':id}
# #     resp = requests.get(BASE_URL+END_POINT,data=json.dumps(data))    
# #     print(resp.status_code) # data is passing to views 
# #     print(resp.json())

# # # get_resourse() # Empty means all record  get_resourse(3)
# # get_resourse(3)



# # def create_ressourse():
# #     new_emp = {
# #         'eno':105,
# #         'ename':'pinny',
# #         'esal':18000,
# #         'eaddr':'Vja'

# #     }
# #     resp = requests.post(BASE_URL+END_POINT,data=json.dumps(new_emp))
# #     print(resp.status_code)
# #     print(resp.json())

    
# #todo -  3/6/2025  Next vidoes 

# # def update_resourse(id):
# #     new_emp = {
# #         'id':id,
# #         'esal':5001 ,
# #         'eaddr':'Hyd'
# #     }
# #     resp = requests.put(BASE_URL + END_POINT, data=json.dumps(new_emp))
# #     print(resp.status_code)
# #     print(resp.json())
# #     # print(resp.text)
# # update_resourse(1)


# # def update_resourse(id):
# #     new_emp = {
# #         'id': id,
# #         'esal': 5001,
# #         'eaddr': 'Hyd'
# #     }
# #     resp = requests.put(BASE_URL + END_POINT, json=new_emp)

# #     print(resp.status_code)
# #     print(resp.json())   # ✔ now this works

# # update_resourse(1)


# # def update_resourse(id):
# #     new_emp = {
# #         'id': id,
# #         'ename':'sunny', # here we are not passing the ename it gives an Error 
# #         'esal': 50001,
# #         # 'eaddr': 'Delhi'
# #     }
# #     resp = requests.put(BASE_URL + END_POINT, json=new_emp)

# #     print(resp.status_code)
# #     print(resp.json())   
# # update_resourse(12)

# def update_resourse(id):
#     new_emp = {
#         'id': id,
#         # 'ename':'Bun', # here we are not passing the ename it gives an Error 
#         'ename':'sunny', 
#         # 'esal': 5001,
#         # 'esal': 4000,
#         # 'esal': 40000,
#         'esal': 52000,
#     }
#     resp = requests.put(BASE_URL + END_POINT, json=new_emp)

#     print(resp.status_code)
#     print(resp.json())   

# update_resourse(12)


# 

import time
import requests
import json 

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

# print("GET request")
# def get_resourse(id=None): 
#     data = {}
#     if id is not None:
#         data = {'id':id}
#     resp = requests.get(BASE_URL+END_POINT,data=json.dumps(data))    
#     print(resp.status_code) 
#     print(resp.json())
# get_resourse(3) # here we passing id 

# time.sleep(10)
# print("POST request")
# def create_resource():
#     new_emp = {
#         'eno':107,
#         'ename':'Ridhika',
#         'esal':22000,
#         'eaddr':'Delhi'
#     }
#     resp = requests.post(BASE_URL + END_POINT, data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# create_resource() 

# time.sleep(10)
print("UPDATE Record ")
def update_resourse(id):
    new_emp = {
        'id':id,
        'eno': 103,
        'ename':'SAGAR',
        'esal':12345,
        'eaddr': 'Delhi'
        
    }
    resp = requests.post(BASE_URL + END_POINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
update_resourse(9)
# time.sleep(10)
# print("DELETE Record  ")
# def delete_resourse(id):

#     jdata = {
#         'id':id
#     }
#     resp = requests.delete(BASE_URL + END_POINT, data=json.dumps(jdata))
#     print(resp.status_code)
#     print(resp.json())
# delete_resourse(11)




