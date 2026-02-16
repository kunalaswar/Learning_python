    # todo  - this is your class you have to include in into middleware inside of the setting.py middleware 
class ExecutionFlowMiddleware(object):  
    def __init__(self,get_response):
        print("init method execution......")
        self.get_response = get_response

    def __call__(self, request):
        print("preprocessing of request")
        response = self.get_response(request)
        print("Postprocessing of request    ")
        return response 
    


        