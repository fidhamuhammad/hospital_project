from django.shortcuts import render

# Create your views here.

def doctorhome(request):
    return render(request,'doctor_template/doctorhome.html')

def home(request):
    return render(request,'doctor_template/home.html')

    