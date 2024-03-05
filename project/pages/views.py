from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(request):
    return HttpResponse('<h1> Hey ! how are you </h1>')
def index2(request):
    return HttpResponse('<h2> I am AI student</h2>')