from django.shortcuts import render
from django.http import HttpResponse

def index(request):
     return render(request,'home.html')
     
def analyze(request):
    n1=int(request.POST.get('num1'))
    n2=int(request.POST.get('num2'))

    add=n1+n2
    minus=n1-n2
    mult=n1*n2
    params = {'addition': add, 'subtraction': minus, 'product': mult,'n1':n1,'n2':n2}
    if(n1<n2):
        return render(request,'error.html',params)
    else:
        divi=n1/n2

    params_with_div={'addition':add,'subtraction':minus,'product':mult,'division':divi,'n1':n1,'n2':n2}
    return render(request,'result.html',params_with_div)