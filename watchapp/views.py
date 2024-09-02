from django.urls import path
from django.http import HttpResponse

def Home(request):
    return HttpResponse("hello home")
                        
def About(request):
    return HttpResponse("hello about")