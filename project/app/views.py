from django.shortcuts import render
from .forms import *
from .models import *


# Create your views here.
def home(request):
    context={}
    context['form']=StudentForm
    return render(request,'home.html',context)

def register(request):

    name=request.POST.get('Name')
    email=request.POST.get('Email')
    password=request.POST.get('Password')
    city=request.POST.get('City')

    data=Student.objects.filter(Email=email)
    print(data)

    if data:
        msg="Email already exist" 
        return render(request,'home.html',{'key':msg})
    else:
        Student.objects.create(Name=name,
                                     Email=email,
                                     Password=password,
                                     City=city)
        msg='registrations '

        return render(request,'register.html',{'key':msg})