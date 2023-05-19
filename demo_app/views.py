from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.
def hey(request):
    time.sleep(5)
    return HttpResponse("hey how are you..")