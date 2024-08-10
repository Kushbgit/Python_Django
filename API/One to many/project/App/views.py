from django.shortcuts import render
from django.http import HttResponse
from .models import Students
# Create your views here.
def home(request):
    return HttResponse("Student")