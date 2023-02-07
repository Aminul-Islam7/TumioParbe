from django.shortcuts import render

# Create your views here.


def home(request,):
    return render(request, 'core/home2.html')

def course1(request):
    return render(request, 'core/course1.html')

def course2(request):
    return render(request, 'core/course2.html')

def awards(request):
    return render(request, 'core/awards.html')
