from django.http import HttpResponse, request
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'main/home.html',{'name':'home','num': 1})

def about(request):
    return render(request, 'main/about.html',{'name':'about us','num': 2})

def contact(request):
    return render(request, 'main/contact.html',{'name':'contact us','num': 3})

