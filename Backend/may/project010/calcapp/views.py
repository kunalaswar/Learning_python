from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# Create your views here.
def calculator(request):
    num1 = eval(request.GET.get("n1"))
    num2 = eval(request.GET.get("n2"))
    cmd = request.GET.get("b1")
    match(cmd):
        case "Add":
            num3 = num1+num2
        case "Sub":
            num3 = num1-num2
        case "Mul":
            num3 = num1*num2
        case "Div":
            num3 = num1/num2
    dict1 = {'num1':num1,"num2":num2,"num3":num3}
    response = render(request,"result.html",context = dict1)
    return response 
#! Ha function display karate na templates sathi aahe 
def index(request):
    response = render(request,"calc.html",context={})
    return response