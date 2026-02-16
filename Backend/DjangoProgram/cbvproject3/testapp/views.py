from django.shortcuts import render

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Company
# Create your views here.
class CompanyList(ListView):
    model  = Company    

#^ Default template file name:company_list.html
#^ Default context object name:company_list

class CompanyDetailView(DetailView):
    model = Company

# template file name:company_detail.html
# context object name:company or object    


class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'
#todo -for Creating the info we have a form so that here we have to Create an html file with name with 
#todo - template file name:company_form.html

class CompanyUpdateView(UpdateView):
    model = Company
    fields=('location','ceo')
from django.urls import reverse_lazy
class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('list')




    
