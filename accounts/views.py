from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<strong>Home Page<strong>")

def product(request):
    return HttpResponse("Product Page")

def customer(request):
    return HttpResponse("Customer Page")