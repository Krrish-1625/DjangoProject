from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page_view(request):
    return HttpResponse("Hello Krushna, welcome to the Earth")

def about_page_view(request):
    return render (request,"about.html")
