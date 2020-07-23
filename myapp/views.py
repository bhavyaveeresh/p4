from django.shortcuts import render
from django.htpp import HttpResponse
from math import factorial
# Create your views here.

def index(request):
    return HttpResponse("<h1>welcome to views of app</h1>")

def home(request):
    return render(request,"myapp/home.html",{'name':"bhavya"})

def fact(request,n):
    n=int(n)
    return HttpsResponse("<h4>factorial is {}</h4>",format(factorial(n)))