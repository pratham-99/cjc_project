from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Customer, AllOrder
from .forms import StudentForm, CustomerForm, AllOrderForm


def home(request):
    return render(request, template_name='index.html')

def addCustomer(request):
    if request.method == 'POST':
        n = request.POST['cname']
        a = request.POST['caddr']
        e = request.POST['cemail']
        p = request.POST['cphone']
        c = Customer(cname=n, caddr=a, cemail=e, cphone=p)
        c.save()
        return redirect('/ecomm/allc/')
    elif request.method == 'GET':
        print('Get request received')
        template_name = 'ecommerce/add_cust.html'
        context = {}
        return render(request, template_name, context)


def allCustomer(request):
    cust = Customer.objects.all()
    template_name = 'ecommerce/allcustomer.html'
    context = {'cust': cust}
    return render(request, template_name, context)


def addStudent(request):
    stu = StudentForm()
    template_name = 'ecommerce/add_stu.html'
    context = {'form':stu}
    return render(request, template_name, context)


def addCustomerDj(request):
    if request.method == 'POST':
        print('POST request received for addcustomer')
        cust = CustomerForm(request.POST)
        if cust.is_valid():
            n = cust.cleaned_data['cname']
            a = cust.cleaned_data['caddr']
            e = cust.cleaned_data['cemail']
            m = cust.cleaned_data['cphone']
            cust_obj = Customer(cname=n, caddr=a, cemail=e, cphone=m)
            cust_obj.save()
            return redirect('/ecomm/allc/')
    else:
        print('get req rec')
        cust = CustomerForm()
        template_name = 'ecommerce/add_custDJ.html'
        context = {'form':cust}
        return render(request, template_name, context)


@login_required
def addOrder(request):
    if request.method == 'POST':
        ord = AllOrderForm(request.POST)
        if ord.is_valid():
            # n = ord.cleaned_data['name']
            # b = ord.cleaned_data['batch_no']
            # q = ord.cleaned_data['qty']
            # p = ord.cleaned_data['price']
            # ord_obj = AllOrder(name=n, batch_no=b, qty=q, price=p)
            # ord_obj.save()
            ord.save()
            return redirect('/ecomm/allo/')
    else:
        ord = AllOrderForm()
        template_name = 'ecommerce/add_orderDJ.html'
        context = {'form':ord}
        return render(request, template_name, context)


def allOrder(request):
    order = AllOrder.objects.all()
    template_name = 'ecommerce/allorders.html'
    context = {'form':order}
    return render(request, template_name, context)

def deleteOrder(request,oid):
    ord = AllOrder.objects.get(pk=oid)
    ord.delete()
    return redirect('/ecomm/allo/')

def updateOrder(request,oid):
    ord = AllOrder.objects.get(pk=oid)
    if request.method == 'GET':
        ord_obj = AllOrderForm(instance=ord)
        template_name = 'ecommerce/all_orderDJ.html'
        context = {'form':ord_obj}
        return render(request, template_name, context)
    elif request.method == 'POST':
        ord_obj = AllOrderForm(request.POST, instance=ord)
        ord_obj.save()
        return redirect('allorder')

def registrationView(request):
    if request.method == 'GET':
        reg = UserCreationForm()
        context = {'form':reg}
        template_name = 'ecommerce/registration.html'
        return render(request, template_name, context)
    elif request.method == 'POST':
        reg = UserCreationForm(request.POST)
        reg.save()
        return redirect('home')


def loginView(request):
    if request.method == 'GET':
        return render(request, template_name='ecommerce/login.html')
    elif request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pword']
        user = authenticate(username=u, password=p)

        if user is not None:
            login(request,user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('home')
        else:
            context = {}
            messages.error(request, 'Invalid Credentials!!')
            template_name = 'ecommerce/login.html'
            return render(request, template_name, context)


def logoutView(request):
    logout(request)
    return redirect('login')

def contact(request):
    return render(request, template_name= 'contact.html')


