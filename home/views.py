from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def loginPage(request):
    # return render(request, 'login_page.html')
    return render(request, 'home/login_page.html')

def receipe_page(request):
    return render(request, 'home/receipes.html')

def register(request):
    return render(request, 'home/register.html')
