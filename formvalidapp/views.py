from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.

def newStudent(request):
    if request.method == 'POST':
        stud = StudentForm(request.POST)
        if stud.is_valid():
            r = stud.cleaned_data['rn']
            n = stud.cleaned_data['name']
            m = stud.cleaned_data['marks']
            p2 = stud.cleaned_data['password2']
            student = Student(rn=r, name=n, marks=m, pw=p2)
            student.save()
            return redirect(allStudents)
    elif request.method == 'GET':
        stud = StudentForm()
    template_name = 'formvalidapp/valid.html'
    context = {'form':stud}
    return render(request, template_name, context)

def allStudents(request):
    allstu = Student.objects.all()
    template_name = 'formvalidapp/allstu.html'
    context = {'form':allstu}
    return render(request, template_name, context)
