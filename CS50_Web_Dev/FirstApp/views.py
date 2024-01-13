from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):  # HTTP request
    return HttpResponse("Hello, World!")

def jack(request):
    return HttpResponse("Hello, Jack!")