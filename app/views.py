from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def bharath(request):
    return HttpResponse("bharath is a good boy")

def megana(request):
    return HttpResponse('my name is megana sir....')