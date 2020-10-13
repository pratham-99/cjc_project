from django.http import HttpResponse
from django.shortcuts import render
from .models import Student

# Create your views here.

def view1(request):
    return HttpResponse('<h1>Response from firstapp---view1</h1>')

def view2(request):
    template_name = 'firstapp/1.html'
    return render(request,template_name)


def homeView(request):
    template_name = 'firstapp/home.html'
    context = {}
    return render(request,template_name, context)


def aboutView(request):
    template_name = 'firstapp/about.html'
    context = {}
    return render(request,template_name, context)


def contentView(request):
    template_name = 'firstapp/content.html'
    context = {}
    return render(request,template_name, context)

def allStudents(request):
    s1 = Student(rn=10, name='Sushil', marks=7)
    s2 = Student(name='Priyanka', rn=9, marks=70)
    s2.save()
    s1.save()
    students = Student.objects.all()
    template_name = 'firstapp/allstudents.html'
    context = {'stu':students}
    return render(request, template_name,context)