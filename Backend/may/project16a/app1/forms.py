from django import forms
class RegisterForm(forms.Form):
    uname = forms.CharField(max_length=12)
    password = forms.CharField(max_length=16,widget=forms.PasswordInput())
    cpassword = forms.CharField(max_length=16,widget=forms.PasswordInput())

    def clean_cpassword(self): #todo here d is clean dictionary Data
        d=super().clean() #todo calling clean method of super class and it return clean data
        # if d.['password'] == d.['cpassword']:
        if d.get('password') == d.get('cpassword'):
            return d   
        else:
            print("password does not match ")
            raise forms.ValidationError("Password does not match with confirm password")
        

