from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Book
# Create your views here.
class BookListView(ListView): # parent class takecare Everythings
    model  = Book
    #! default template file name:modelname_list.html
    #! default context object name:modelname_list
     
    # if you want to Create your own Name  context object and Templates name 
    #todo - with the help of this parameter we can give your own name 
    template_name = 'testapp/book.html'

    context_object_name = 'books'

# video 13/5/2025
class BookListView2(ListView):
    model = Book
    template_name = 'testapp/books.html'
    context_object_name = 'books'

class BookDetailView(DetailView):    
    model = Book 

class BookCreateView(CreateView):   
    model  = Book
    fields = ('title','author','pages','price')          
    
# If we send request:
# 	http://127.0.0.1:8000/create/

# We are getting an error:
# 	ImproperlyConfigured at /create/
# 	Using ModelFormMixin (base class of BookCreateView) without the 'fields' attribute is prohibited.
#^ so that we use this field name in side of the Class 
    # fields = ('title','author','pages','price')      
     

class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'

from django.urls import reverse_lazy # it is waiting until deliting the/ your  record
class BookDeleteView(DeleteView):
    model  = Book # model is Book 
    success_url = reverse_lazy('listbooks') # After deleting Which page you want to display



