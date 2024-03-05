from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def prod1(request):
    return HttpResponse('first product')
def prod2(request):
    return HttpResponse('second product')