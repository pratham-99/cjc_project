from django.shortcuts import render

# Create your views here.

def htmlPage(request):
    context = {'name':'Rajani'}
    template_name = 'html_page.html'
    return render(request,template_name, context)

def calcView(request):
    n1 = int(request.POST.get('num1',0))
    n2 = int(request.POST.get('num2',0))
    tot = n1 + n2 #tot = 0 + 0

    content = {'total':tot} #context = {'total': 0}
    template_name = "secondapp/calc.html"
    return render(request, template_name, content)
