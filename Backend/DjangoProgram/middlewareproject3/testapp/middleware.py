from django.http import HttpResponse
class ErrorMessageMiddleware(object):
        # You're creating middleware to handle ERRORS gracefully
    # Shows friendly message instead of ugly error pages
    def __init__(self,get_response): # run automatically beacuse it is a constructure 
          # This runs ONCE when Django starts
        self.get_response = get_response 
         # You're storing get_response (next middleware or view)
    
    def __call__(self, request): # Runs for EVERY request
        response = self.get_response(request)
        return response 

    def process_exception(self,request,exception):# this run when the Error is come 
        # return HttpResponse('<h1>Currently we are facing some techincal problem ....Pls try sometime</h1>')
        return HttpResponse(f'<h1>Currently we are facing some techincal problem <br> The Raised Exception:{exception.__class__.__name__}</h1>')
    

# class ErrorMessageMiddleware(object):
#     # You're creating middleware to handle ERRORS gracefully
#     # Shows friendly message instead of ugly error pages
    
#     def __init__(self, get_response):
#         # This runs ONCE when Django starts
#         self.get_response = get_response
#         # You're storing get_response (next middleware or view)
    
#     def __call__(self, request):
#         # This runs on EVERY request
        
#         response = self.get_response(request)
#         # You're calling the VIEW (letting request continue)
#         # If view works → response contains view's result
#         # If view crashes → process_exception() runs automatically
        
#         return response
#         # You're returning the view's response to user
    
#     def process_exception(self, request, exception):
#         # This runs ONLY when an error/exception occurs in views
#         # exception = the error that happened
        
#         return HttpResponse(f'<h1>Currently we are facing some technical problem <br> The Raised Exception: {exception.__class__.__name__}</h1>')
#         # You're showing friendly error message instead of crash page
#         # exception.__class__.__name__ = name of the error (e.g., "ValueError", "ZeroDivisionError")        