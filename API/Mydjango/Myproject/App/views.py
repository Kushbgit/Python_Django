from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from .models import Students

# Create your views here.
def Home(request):
    return HttpResponse("<h1>Welcome to this Page</h1>")

def Register(request):
    return render(request,'register.html')
    

def Registerdata(request):
    print(request.method)
    print(request.POST)
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    print(name,email,contact)
    Students.objects.create(Name=name,Email=email,Contact=contact)
    print("Data save Succesfully")
    

def homepage(request):
    return render(request,'homepage.html')
def landing(request):
    return render(request,'landing.html')
def about(request):
    return render(request,'aboutpage.html')
def contact(request):
    return render(request,'contact.html')
# def registered(request):
    return render(request,'registered.html')