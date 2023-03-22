from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Car
from .forms import CarForm

# Create your views here.

def home(request):
    cars = Car.objects.all()
    context={'cars': cars}
    return render(request,'home.html',context)

def say_hello(request):
    return render(request, 'hello.html')


def car(request, pk):
    car=Car.objects.get(id=pk)
    context={'car': car}
    return render(request,'car.html',context)

def createCar(request):
    form= CarForm()
    if request.method == "POST":
        form=CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request, 'car_form.html',context)

def updateCar(request, pk):
    car=Car.objects.get(id=pk)
    form=CarForm(instance=car)
    if request.method == "POST":
        form=CarForm(request.POST,instance=car)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form': form}
    return render(request,'car_form.html',context)
    
def deleteCar(request,pk):
    car=Car.objects.get(id=pk)
    if request.method=="POST":
        car.delete()
        return redirect('home')
    return render(request,'delete.html',{'obj':car})