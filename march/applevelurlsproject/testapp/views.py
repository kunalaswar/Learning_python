from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def exam_view(request):
    return HttpResponse("<h1>Exams Views</h1>")
def attendance_view(request):
    return HttpResponse("<h1>Attendence Views</h1>")
def fees_view(request):
    return HttpResponse("<h1>Fees Views</h1>")
