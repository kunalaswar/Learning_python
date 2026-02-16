# from django.shortcuts import render
# from rest_framework.views import APIView #^# You're importing APIView - base class for creating REST API views
# from rest_framework.response import Response # this class is to convert python dict to json data
# class TestAPIView(APIView):
  #^# Response = automatically converts Python dictionary to JSON  No need for JSONRenderer anymore!
#     def get(self,request,*args,**kwargs):
#         colors = ['RED','YELLOW','GREEN','BLUE']

#         return Response({'msg':'Happy Valentines Day....','colors':colors})#Response class is responsible to convert python dict to json_data
    
#     def put(self,request):
#         return Response({'msg':'This response fron PUT method APIView'})
    
#     def delete(self,request):
#         return Response({'msg':'This response fron DELETE method APIView'})
    
#     def patch(self,request):
#         return Response({'msg':'This response fron PATCH method APIView'})
    
#todo - 4/6/2025
from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.response import Response # this class is to convert python dict to json data
from rest_framework.viewsets import ViewSet
class TestViewSet(ViewSet):
    def list(self,request):
        colors = ['RED','YELLOW','GREEN','BLUE']
        return Response({'msg':'RCB Won the IPL Cup','colors':colors})
    
    def retrieve(self,request,pk=None  ):
        return Response({'msg':'This Response from RETRIEVE method ViewSet'})
    
    def update(self,request,pk = None):
        return Response({'msg':'This Response from UPDATE method ViewSet'})
    def partial_update(self,request,pk=None):
        return Response({'msg':'This Response from Partial_update method ViewSet'})
    
    def destroy(self,request,pk=None):
        return Response({'msg':'This Response from RETRIEVE method ViewSet'})










# class TestAPIView(APIView):

#     def get(self,request,*args,**kwargs):
#         colors = ['RED','YELLOW','GREEN','BLUE']

#         return Response({'msg':'Happy Valentines Day....','colors':colors})#Response class is responsible to convert python dict to json_data
    
#     def put(self,request):
#         return Response({'msg':'This response fron PUT method APIView'})
    
#     def delete(self,request):
#         return Response({'msg':'This response fron DELETE method APIView'})
    
#     def patch(self,request):
#         return Response({'msg':'This response fron PATCH method APIView'})
    
