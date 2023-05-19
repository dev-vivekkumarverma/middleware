import time


class timeMiddleware:
    def __init__(self,get_response) -> None:
        self.get_response=get_response
    def __call__(self,request):
        start_time=time.time()
        response=self.get_response(request)
        total_time=(time.time()-start_time)*1000
        print("total round trip time (in ms):",total_time)
        return response
