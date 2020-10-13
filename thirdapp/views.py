from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def view1(request):
    return HttpResponse('Response from thiedapp----view1')