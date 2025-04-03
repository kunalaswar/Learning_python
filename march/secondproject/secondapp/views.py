from django.shortcuts import render
from django.http import HttpResponse   
# Create your views here.   

def display(request):
    s = '''
    <h1>Welcome to my Second Django application </h2><hr><button <button  color: white;">Click me!</button>
        <form method="post">
        
        <label for="first_name">First Name:</label>
        <input type="text" id="first_name" name="first_name" >
        <br></br>

        <label for="last_name">Last Name:</label>
        <input type="text" id="last_name" name="last_name" >
        <br></br>

        <input type="submit" value="Submit">
        </form>'''

    return HttpResponse(s)
