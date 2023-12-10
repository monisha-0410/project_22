from django.shortcuts import render

# Create your views here.

def example(request):
    return render(request,'example.html')

def control(request):
    return render(request,'control.html')

def indicator(request):
    return render(request,'indicator.html')


def caption(request):
    return render(request,'caption.html')