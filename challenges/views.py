from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    return HttpResponse('My First Website')

def monthlyy(request, month):
    
        return HttpResponse(f"{month}challenges")