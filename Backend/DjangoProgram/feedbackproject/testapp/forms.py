# from django import forms
# from django.core import validators
# def start_with_s(value):
#     print('Start_with_s function Execution')
#     if value[0].lower() !='s':
#         raise forms.ValidationError('Name should be start with S or s ')
# class FeedBackForm(forms.Form):
#     name  = forms.CharField(start_with_s) # user-defined validators    
#     rollno = forms.IntegerField()
#     email  = forms.EmailField()
#     feedback = forms.CharField(widget=forms.Textarea,validators=[
# 	validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
    
    # def clean_name(self):
    #     print('Validaning Name Field')
    #     input_name = self.cleaned_data['name']
    #     if len(input_name) < 4:
    #         raise forms.ValidationError('The minimum number of characters in the name filed should be 4')
    #     return input_name
    # def clean_rollno(self):
    #     print("Validating the Rollno Filed")
    #     input_rollno = self.cleaned_data['rollno']
    #     return input_rollno
    # def clean_email(self):
    #     print("Validating of Email Field")
    #     input_email = self.cleaned_data['email']
    #     return   input_email
    # def clean_feedback(self):
    #     print("Valaditing Feedback Field")
    #     input_feedback = self.cleaned_data['feedback']
    #     return input_feedback

from django import forms
from django.core import validators  
# video 3
# class FeedBackForm(forms.Form):
#     name  = forms.CharField()
#     rollno = forms.IntegerField()
#     email  = forms.EmailField()
#     feedback = forms.CharField(widget=forms.Textarea)

#     def clean(self):
#         print("Total Form Validations") 
#         total_clearn_data=super().clean() # super calling the parent class method 
#         print('Validating Name')
#         input_name = total_clearn_data['name']# predefined method 
#         if input_name[0].lower() != 's':
#             raise forms.ValidationError("Name should start with s letter ")
#         print('Validating Roll No')
#         input_rollno = total_clearn_data['rollno']
#         if input_rollno <=0:
#             raise forms.ValidationError("Rollno should be greater than Zero ")
#         print('Validating Email')
#         input_email = total_clearn_data['email']
#         if input_email[-10:] !='@gmail.com':
#             raise forms.ValidationError("Email Extension should be @gmail.com")
            

# How to Check the original Password and re-Enterpassword is same of not 

# class FeedBackForm(forms.Form):
#     name  = forms.CharField()
#     rollno = forms.IntegerField()
#     email  = forms.EmailField()
#     password = forms.CharField(label="Enter Password:",widget=forms.PasswordInput)
#     rpassword = forms.CharField(label="Password(Again):",widget=forms.PasswordInput)
#     feedback = forms.CharField(widget=forms.Textarea)

#     def clean(self):
#         total_clearn_data=super().clean()
#         pwd = total_clearn_data['password']
#         rpwd = total_clearn_data['rpassword']
#         if pwd!=rpwd: 
#             raise forms.ValidationError("Both Password must be same")
        



class FeedBackForm(forms.Form):
    name  = forms.CharField()
    rollno = forms.IntegerField()
    email  = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    bot_handler = forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        total_cleaned_data =  super().clean()
        bot_handler_value = total_cleaned_data['bot_handler']
        if len(bot_handler_value)>=0:
            raise forms.ValidationError("Request form Bot cant be submitted")
        

        
        
        

    