from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def courses(request):
    return HttpResponse('What is your course?')

def course(request):
    return HttpResponse('BSIT')




