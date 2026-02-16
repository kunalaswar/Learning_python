# # from django.shortcuts import render

# # # Create your views here.
# # from django.views.generic import View
# # import io
# # from testapp.models import Employee
# # from testapp.serializers import EmployeeSerializer
# # from rest_framework.parsers import JSONRenderer
# # from django.http import HttpResponse
# # class EmployeeCRUDCBV(View):
# #     def get(self,request,*args,**kwargs):
# #         json_data = request.body # here  iam reading the data from get method 
# #         stream = io.BytesIO(json_data)
# #         pdata = JSONParser().parse(stream)
# #         id = pdata.get('id',None)
# #         if id is not None:
# #             emp = Employee.objects.get(id = id ) # complex type 
# #             serializer = EmployeeSerializer(emp)
# #             json_data = JSONRenderer().render(serializer.data)
# #             return HttpResponse(json_data,content_type = 'application/json',status=200)
# #         qs = Employee.objects.all()




# import io
# from django.views.generic import View
# from rest_framework.parsers import  JSONParser
# from testapp.models import Employee
# from testapp.serializers import EmployeeSerializer
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# # csrf token only for this class not for Entire class 

# # @method_decorator(csrf_exempt,name='dispatch') # dispatch  this method is applicaple to post method 
# # class EmployeeCRUDCBV(View):
# # from django.shortcuts import render

# # # Create your views here.
# # from django.views.generic import View
# # import io
# # from testapp.models import Employee
# # from testapp.serializers import EmployeeSerializer
# # from rest_framework.parsers import JSONRenderer
# # from django.http import HttpResponse
# # class EmployeeCRUDCBV(View):
# #     def get(self,request,*args,**kwargs):
# #         json_data = request.body # here  i am reading the data from get method 
# #         stream = io.BytesIO(json_data)
# #         pdata = JSONParser().parse(stream)
# #         id = pdata.get('id',None)
# #         if id is not None:
# #             emp = Employee.objects.get(id = id ) # complex type 
# #             serializer = EmployeeSerializer(emp)
# #             json_data = JSONRenderer().render(serializer.data)
# #             return HttpResponse(json_data,content_type = 'application/json',status=200)
# #         qs = Employee.objects.all()


#^ json_data = JSONRenderer().render(serializer.data)
# You're converting Python dictionary to JSON string
# JSONRenderer() = Django REST Framework's tool to create JSON
# .render() = converts data to JSON format
# serializer.data = Python dictionary from serializer   


# # @method_decorator(csrf_exempt,name='dispatch') # dispatch  this method is applicaple to post method 
# class EmployeeCRUDCBV(View):
#     def delete(self,request,*args,**kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pdata = JSONParser().parse(stream)
#         id =pdata.get('id') # from python data read that id 
#         emp = Employee.objects.get(id=id)
#         emp.delete() # who i am getting the record just delete it 
#         msg = {'msg':'Resourse deleted successfully '}
#         json_data = JSONRenderer().render(msg)
#         return HttpResponse(json_data,content_type = 'application/json')


# # @method_decorator(csrf_exempt,name='dispatch') # dispatch  this method is applicaple to post method 
# # class EmployeeCRUDCBV(View):
#     def put(self,request):
#         json_data=request.body # reading json data
#         stream = io.BytesIO(json_data)
#         pdata =  JSONParser().parse(stream)
#         id = pdata.get('id')   
#         #* once python data available get the id 
#         #* which record you want to change pass his id beacuse method is put 
#         emp = Employee.objects.get(id=id)
#         # the emp you send to the employee class
#         serializer = EmployeeSerializer(emp,data = pdata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             msg = {'msg':'Resourse Updated  Successfully.........'}
#             json_data  = JSONRenderer().render(msg) # dict i want to convert Json data
#             return HttpResponse(json_data,content_type = 'application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type = 'application/json',status = 400)
    
# #?   ===========CHATGPT==========================

#     # # @method_decorator(csrf_exempt,name='dispatch') # dispatch  this method is applicaple to post method 
#     # def post(self,request,*args,**kwargs):
#     #     json_data = request.body
#     #     stream = io.BytesIO(json_data) # this is converted to string file  
#     #     pdata = JSONParser().parse(stream) # data is in pythondict
#     #     serializer = EmployeeSerializer(data = pdata)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         msg = {'msg':'Resourse created Successfully.........'}
#     #         json_data  = JSONRenderer().render(msg) # dict i want to convert Json data
#     #         return HttpResponse(json_data,content_type = 'application/json')
#     #     json_data = JSONRenderer().render(serializer.errors)
#     #     return HttpResponse(json_data,content_type = 'application/json',status = 400)
    


#     def get(self,request):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         # pdata = JSONParser().parse(stream)
#         pdata = request.GET
#         id = pdata.get('id',None)
#         if id is not None:
#             emp = Employee.objects.get(id=id)
#             serializer = EmployeeSerializer(emp)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         qs = Employee.objects.all()   
#         eserializer = EmployeeSerializer(qs, many=True)
#         json_data = JSONRenderer().render(eserializer.data)
#         return HttpResponse(json_data, content_type='application/json')



# # @method_decorator(csrf_exempt,name='dispatch') # dispatch  this method is applicaple to post method 
# # class EmployeeCRUDCBV(View):
#     # def put(self,request):
#     #     json_data=request.body # reading json data
#     #     stream = io.BytesIO(json_data)
#     #     pdata =  JSONParser().parse(stream)
#     #     id = pdata.get('id')   
#     #     #* once python data available getthe id 
#     #     #* which record you want to change pass his id 
#     #     emp = Employee.objects.get(id=id)
#     #     # the emp you send to the employee class
#     #     serializer = EmployeeSerializer(emp,data = pdata,partial=True)
#     #     if serializer.is_valid():
#     #         serializer.save()   
#     #         msg = {'msg':'Resourse Updated  Successfully.........'}
#     #         json_data  = JSONRenderer().render(msg) # dict i want to convert Json data
#     #         return HttpResponse(json_data,content_type = 'application/json')
#     #     json_data = JSONRenderer().render(serializer.errors)
#     #     return HttpResponse(json_data,content_type = 'application/json',status = 400)
    
# #?   ===========CHATGPT==========================

#     # @method_decorator(csrf_exempt,name='dispatch') # dispatch  this method is applicaple to post method 
#     def post(self,request,*args,**kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data) # this is converted to string file  
#         pdata = JSONParser().parse(stream) # data is in pythondict
#         serializer = EmployeeSerializer(data = pdata)
#         if serializer.is_valid():
#             serializer.save()
#             msg = {'msg':'Resourse created Successfully.........'}
#             json_data  = JSONRenderer().render(msg) # dict i want to convert Json data
#             return HttpResponse(json_data,content_type = 'application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type = 'application/json',status = 400)
    


#     # def get(self,request):
#     #     json_data = request.body
#     #     stream = io.BytesIO(json_data)
#     #     # pdata = JSONParser().parse(stream)
#     #     pdata = request.GET
#     #     id = pdata.get('id',None)
#     #     if id is not None:
#     #         emp = Employee.objects.get(id=id)
#     #         serializer = EmployeeSerializer(emp)
#     #         json_data = JSONRenderer().render(serializer.data)
#     #         return HttpResponse(json_data,content_type='application/json')
#     #     qs = Employee.objects.all()
#     #     eserializer = EmployeeSerializer(qs, many=True)
#     #     json_data = JSONRenderer().render(eserializer.data)
#     #     return HttpResponse(json_data, content_type='application/json')

#     # from django.shortcuts import render

# # # Create your views here.
# # from django.views.generic import View
# # import io
# # from testapp.models import Employee
# # from testapp.serializers import EmployeeSerializer
# # from rest_framework.parsers import JSONRenderer
# # from django.http import HttpResponse
# # class EmployeeCRUDCBV(View):
# #     def get(self,request,*args,**kwargs):
# #         json_data = request.body # here  i am reading the data from get method 
# #         stream = io.BytesIO(json_data)
# #         pdata = JSONParser().parse(stream)
# #         id = pdata.get('id',None)
# #         if id is not None:
# #             emp = Employee.objects.get(id = id ) # complex type 
# #             serializer = EmployeeSerializer(emp)
# #             json_data = JSONRenderer().render(serializer.data)
# #             return HttpResponse(json_data,content_type = 'application/json',status=200)
# #         qs = Employee.objects.all()




# # import io
# # from django.views.generic import View
# # from rest_framework.parsers import  JSONParser
# # from testapp.models import Employee
# # from testapp.serializers import EmployeeSerializer
# # from rest_framework.renderers import JSONRenderer
# # from django.http import HttpResponse
# # from django.views.decorators.csrf import csrf_exempt
# # from django.utils.decorators import method_decorator
# # # csrf token only for this class not for Entire class 



# # # @method_decorator(csrf_exempt,name='dispatch') # dispatch  this method is applicaple to post method 
# # class EmployeeCRUDCBV(View):
# #     def get(self,request):
# #         json_data = request.body
# #         stream = io.BytesIO(json_data)
# #         # pdata = JSONParser().parse(stream)
# #         pdata = request.GET
# #         id = pdata.get('id',None)
# #         if id is not None:
# #             emp = Employee.objects.get(id=id)
# #             serializer = EmployeeSerializer(emp)
# #             json_data = JSONRenderer().render(serializer.data)
# #             return HttpResponse(json_data,content_type='application/json')
# #         qs = Employee.objects.all()
# #         eserializer = EmployeeSerializer(qs, many=True)
# #         json_data = JSONRenderer().render(eserializer.data)
# #         return HttpResponse(json_data, content_type='application/json')
    
# #     def post(self,request,*args,**kwargs):
# #         json_data = request.body
# #         stream = io.BytesIO(json_data) # this is converted to string file  
# #         pdata = JSONParser().parse(stream) # data is in pythondict
# #         serializer = EmployeeSerializer(data = pdata)
# #         if serializer.is_valid():
# #             serializer.save()
# #             msg = {'msg':'Resourse created Successfully.........'}
# #             json_data  = JSONRenderer().render(msg) # dict i want to convert Json data
# #             return HttpResponse(json_data,content_type = 'application/json')
# #         json_data = JSONRenderer().render(serializer.errors)
# #         return HttpResponse(json_data,content_type = 'application/json',status = 400)
    

# #     def put(self,request):
# #         json_data=request.body # reding json data
# #         stream = io.BytesIO(json_data)
# #         pdata =  JSONParser().parse(stream)
# #         id = pdata.get('id')   
# #         # once python data available getthe id 
# #         # which record you want to change pass his id 
# #         emp = Employee.objects.get(id=id)
# #         # the emp you send to the employee class
# #         serializer = EmployeeSerializer(emp,data = pdata,partial=True)
# #         if serializer.is_valid():
# #             serializer.save()
# #             msg = {'msg':'Resourse Updated  Successfully.........'}
# #             json_data  = JSONRenderer().render(msg) # dict i want to convert Json data
# #             return HttpResponse(json_data,content_type = 'application/json')
# #         json_data = JSONRenderer().render(serializer.errors)
# #         return HttpResponse(json_data,content_type = 'application/json',status = 400)
    
# # #?   ===========CHATGPT==========================

# #     # @method_decorator(csrf_exempt,name='dispatch') # dispatch  this method is applicaple to post method 
# #     def delete(self,request,*args,**kwargs):
# #         json_data = request.body
# #         stream = io.BytesIO(json_data)
# #         pdata = JSONParser().parse(stream)
# #         id =pdata.get('id') # from python data read that id 
# #         emp = Employee.objects.get(id=id)
# #         emp.delete() # who i am getting the record just delete it 
# #         msg = {'msg':'Resourse deleted successfully '}
# #         json_data = JSONRenderer().render(msg)
# #         return HttpResponse(json_data,content_type = 'application/json')




import io
from django.views.generic import View
from django.http import HttpResponse

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from testapp.models import Employee
from testapp.serializers import EmployeeSerializer


# csrf_exempt is applied to the whole class
# so POST / PUT / DELETE can work from requests or Postman
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(View):

    # ===================== GET =====================
    # Used to READ data
    # If id is given → single record
    # If id is not given → all records
    def get(self, request):
        # GET data always comes from URL (query params)
        # example: /api/?id=3
        id = request.GET.get('id')

        if id is not None:
            # get single employee record
            emp = Employee.objects.get(id=id)

            # convert model object → python dict
            serializer = EmployeeSerializer(emp)

            # convert python dict → json
            json_data = JSONRenderer().render(serializer.data)

            return HttpResponse(json_data, content_type='application/json')

        # if id is not provided → get all employees
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs, many=True)
        json_data = JSONRenderer().render(serializer.data)

        return HttpResponse(json_data, content_type='application/json')

    # ===================== POST =====================
    # Used to CREATE new record
    def post(self, request):
        # POST data comes in request.body as JSON
        # request.body = b'{"eno":101,"ename":"Ram"}'
        stream = io.BytesIO(request.body)

        # JSON → Python dict
        pdata = JSONParser().parse(stream)

        # pass python data to serializer
        serializer = EmployeeSerializer(data=pdata)

        if serializer.is_valid():
            serializer.save()  # inserts record into DB

            msg = {'msg': 'Resource created successfully'}
            json_data = JSONRenderer().render(msg)

            return HttpResponse(
                json_data,
                content_type='application/json',
                status=201
            )

        # if validation fails
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(
            json_data,
            content_type='application/json',
            status=400
        )

    # ===================== PUT =====================
    # Used to UPDATE existing record
    def put(self, request):
        stream = io.BytesIO(request.body)
        pdata = JSONParser().parse(stream)

        # id must be sent from client to know which record to update
        id = pdata.get('id')

        # get existing record
        emp = Employee.objects.get(id=id)

        # partial=True → allow partial update (not all fields required)
        serializer = EmployeeSerializer(emp, data=pdata, partial=True)

        if serializer.is_valid():
            serializer.save()

            msg = {'msg': 'Resource updated successfully'}
            json_data = JSONRenderer().render(msg)

            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(
            json_data,
            content_type='application/json',
            status=400
        )

    # ===================== DELETE =====================
    # Used to DELETE record
    def delete(self, request):
        stream = io.BytesIO(request.body)
        pdata = JSONParser().parse(stream)

        # id tells which record to delete
        id = pdata.get('id')

        emp = Employee.objects.get(id=id)
        emp.delete()

        msg = {'msg': 'Resource deleted successfully'}
        json_data = JSONRenderer().render(msg)

        return HttpResponse(json_data, content_type='application/json')
