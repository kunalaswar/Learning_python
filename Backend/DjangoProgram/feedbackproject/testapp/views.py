from django.shortcuts import render
from testapp.forms import  FeedBackForm
# Create your views here.
def feedback_view(request):
    submitted = False
    name = ''
    form = FeedBackForm()
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        #^ programmer defined validator and there is also built in validaltors 
        #^ this is call Explicitly by prorammmer by using clean method 
        if form.is_valid():
            print('Form validation success and printing feedback information')
            print('*'*55)
            print('Name:',form.cleaned_data['name'])
            print('RollNo:',form.cleaned_data['rollno'])
            print('Mail ID:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback'])
            submitted = True
            name = form.cleaned_data['name']
        # else:

    
    return render(request,'testapp/feedback.html', {'form':form, 'submitted':submitted,'name':name})