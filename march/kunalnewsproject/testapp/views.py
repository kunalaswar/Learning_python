from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,template_name='testapp/index.html')

def movies_info(request):
    # return render(request,template_name=    )
    head_msg = 'Movies Information'
    sub_msg1 = 'MAD square is very good movie'
    sub_msg2 = 'OG will come very soon........'
    sub_msg3 = 'Shaava movie with vikky kaushal'
    type = "movies"
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,template_name='testapp/news.html',context= my_dict) 

def sports_info(request):
    head_msg = 'Sports Informations'
    sub_msg1 = 'Present IPL is going on'
    sub_msg2 = 'Yesterday own the match by RCB'
    sub_msg3 = 'Today matchs was KKR vs LSG'
    type = 'sports'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,template_name='testapp/news.html',context=my_dict)

def politics_info(request):
    head_msg = 'Politics Informations'
    sub_msg1 = 'India PM was Modi ji'
    sub_msg2 = 'AP CM was Chandra Badu Naidu'
    sub_msg3 = 'MH cm was Devendra Fadnavis'
    type = 'politics'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,"type":type}
    return render (request,template_name='testapp/news.html',context=my_dict)
