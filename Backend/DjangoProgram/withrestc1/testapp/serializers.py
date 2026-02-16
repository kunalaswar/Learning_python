from rest_framework import serializers
from testapp.models import Employee 
def multiple_of_1000(value):
    print("Validation by validator attribute ")
    if value%1000 !=0:
        raise serializers.ValidationError("Employee salary should be multiple of 1000")

# class EmployeeSerializer(serializers.Serializer):
#     eno = serializers.IntegerField()
#     ename = serializers.CharField(max_length=10)# max_lenght =4 #400 {'ename': ['Ensure this field has no more than 4 characters.']}
#     esal = serializers.FloatField(validators = [multiple_of_1000])
#     eaddr = serializers.CharField(max_length=30)
#     def validate(self, data):
#         ename = data.get('ename')
#         esal = data.get('esal')
#         print('Object level validators ')
#         if ename.lower() == 'sunny':
#             if esal < 50000:
#                 raise serializers.ValidationError('Sunny sal should be minimum 50000')
#         return data 
    
#     def validate_esal(self,value): # method name is fix and value is esal
#         print('Field level validators ')
#         if value < 5000:
#             raise serializers.ValidationError('Employee salary should be minimum 5000')
#                 # module name. class name
#         return value        

 
    # def create(self, validated_data):
    #     return Employee.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.eno = validated_data.get('eno',instance.eno) # instance means corrent Employee
    #     instance.ename = validated_data.get('ename',instance.ename)
    #     instance.esal = validated_data.get('esal',instance.esal)
    #     instance.eaddr= validated_data.get('eaddr',instance.eaddr)
    #     instance.save()
    #     return instance 
    

#todo - instead of doing like this create ,update  we have to create your ModelSerializer class 

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        esal = serializers.FloatField(validators = [multiple_of_1000])
        model = Employee
        fields = '__all__'


