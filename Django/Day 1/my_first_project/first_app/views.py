from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1> This is homepage </h1>")
def contact(request):
    return HttpResponse("<h1> This is Contact Page </h1>")
def about(request):
    return HttpResponse("<h1> This is About Page </h1>")