from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><h1>Welcome to blog</h1></html>')


def about(request):
    return HttpResponse('<html><h1>About</h1></html>')
