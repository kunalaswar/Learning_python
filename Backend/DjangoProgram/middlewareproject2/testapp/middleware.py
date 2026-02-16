from django.http import HttpResponse    
class AppMaintenceMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
            return HttpResponse('<h1>Currently application under Maintenence Pls try after 2Hrs</h1>')
    